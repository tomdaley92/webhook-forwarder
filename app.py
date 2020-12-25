from flask import Flask, jsonify
from flask_cors import CORS
from util import *
import github


app = Flask(__name__)
CORS(app)

def list_webhooks():
    response = {'github': github.filter_webhooks()}
    return jsonify(response)

# dynamically generate routes from 'config.yaml'
for hook in github.get_webhooks():
    app.add_url_rule(
        rule = github.BASE_PATH+hook['path'],
        endpoint = hook['path'],
        view_func = github.receive,
        methods = ['POST'],
    )

# List all current configurations at "/"
app.add_url_rule(
    rule = github.BASE_PATH,
    endpoint = github.BASE_PATH,
    view_func = list_webhooks,
    methods = ['GET']
)  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
