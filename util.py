from flask import jsonify
import json

def json_response(message, code):

    if isinstance(message, dict):
        response = message
    else:
        try:
            response =json.loads(message)
        except:
            response = {'message': message}

    print(f'Response: {response}, {code}')
    return jsonify(response), code
