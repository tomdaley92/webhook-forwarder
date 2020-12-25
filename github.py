from flask import request
from config import Config
from util import *
import requests
import hashlib
import hmac

config = Config()

BASE_PATH = '/github'

REQUIRED_HEADERS = [
    'X-GitHub-Delivery',
    'X-GitHub-Enterprise-Host',
    'X-GitHub-Enterprise-Version',
    'X-GitHub-Event',
    'X-Hub-Signature',
]

def get_webhooks():
    return config.get('github')

def filter_webhooks():
    # remove all sensitive information
    filtered = get_webhooks()
    for hook in filtered:
        hook.pop('secret')

        hook['path'] = BASE_PATH+hook['path']
        
        for push in hook['events']['push']:
            push.pop('key')

    return filtered

def calculate_signature(key, request_body):
    # github signatures are calulcated using hmac sha1
    return 'sha1='+hmac.new(key, request_body, hashlib.sha1).hexdigest()

def verify_signature(key):
    if request.headers['X-Hub-Signature'][:5] == "sha1=":

        expected = request.headers['X-Hub-Signature']

        # calculate hmac sha1 hash with 'key' and the raw request 'body'
        calculated = calculate_signature(
            key.encode(),
            request.data,
        )

        print(f'Header signature: {expected}')
        print(f'Calculated signature: {calculated}')

        # equal?
        return hmac.compare_digest(expected, calculated)

    # fallback
    return request.headers['X-Hub-Signature'] == key

def check_headers(headers):
    for required in REQUIRED_HEADERS:
        if required not in headers:
            return False
    return True

def ping():
    refs = []
    for hook in get_webhooks():
        if BASE_PATH+hook['path'] == request.path:

            if not verify_signature(hook['secret']):
                return json_response('Invalid Signature.', 403)
            
            for push in hook['events']['push']:
                refs.append(push['filter']["ref"])
    
    response = {
        "message": "pong",
        "refs": refs,
    }

    return json_response(response, 202)

def push():
    if 'ref' not in request.json:
        return json_response('No \'ref\' object in JSON body.', 400)

    responses = []
    for hook in get_webhooks():
        if BASE_PATH+hook['path'] == request.path:
            
            if not verify_signature(hook['secret']):
                return json_response('Invalid Signature.', 403)

            for push in hook['events']['push']:
                
                if push['filter']["ref"] == request.json['ref']:
                    print(f'Reference: {request.json["ref"]}')


                    signature = calculate_signature(
                        push['key'].encode(), 
                        request.data, 
                    )
                        
                    responses.append(forward(push['url'], signature))     

    if len(responses) == 1:
        return json_response(responses[0][0], responses[0][1])
    elif len(responses) > 1:
        return json_response(responses, 202)

    return json_response(f'No webhooks found for {request.json["ref"]}.', 202)

def pull():
    # TODO - Pull events
    return json_response('Event not currently supported, but will be soon!', 202)

def process_event(event):
    print(f'Event: {event}')
    
    EVENTS = {
        'ping' : ping,
        'push' : push,
        'pull' : pull,
    }

    if event not in EVENTS:
        return json_response(f'\'{event}\' event is not supported.', 202)
    
    return EVENTS[event]()

def forward(url, signature):
    print(f'Outgoing: {url}')
    print(f'Header Signature: {signature}')
  
    headers = {
        'Content-Type': 'application/json',
    }
    for required in REQUIRED_HEADERS:
        headers[required] = request.headers[required]
    headers['X-Hub-Signature'] = signature

    response = requests.post(
        url=url,
        headers=headers,
        data=request.data,
    )

    return response.text, response.status_code

def receive():
    print(f'Incoming: {request.path}')

    if not check_headers(request.headers):
        return json_response(f'Missing headers. Required: {REQUIRED_HEADERS}', 400)

    return process_event(request.headers["X-GitHub-Event"]) 
