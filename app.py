from flask import Flask, jsonify, request
from datetime import datetime
import json
import os

app = Flask(__name__)

def cast_to_type(val, cast_type):
    # Special case to handle milliseconds
    if cast_type == "ms":
        if type(val) == int or type(val) == float:
            return int(val)*1000
        try:
            return int(datetime.fromisoformat(val).timestamp())*1000
        except (ValueError, TypeError):
            return None
    try:
        return cast_type(val)
    except (ValueError, TypeError):
        return None


@app.route('/transform_request', methods=['POST'])
def transform_request():
    # Validate that data was passed in
    if not request.is_json:
        return jsonify(null=None)

    req = request.get_json()
    print(req)
    response = {}
    # We know that these are always going to be passed in the request
    response["source"] = req['deviceId']
    response["timestamp"] = int(datetime.fromisoformat(req['timestamp']).timestamp())
    response["data"] = {}

    # Let's get rid of device id and timestamp before continuing - this is an O(1) operation in Python
    del req["deviceId"]
    del req["timestamp"]

    # Iterate through request keys for remaining fields
    for key in req:
        key_resp = {}
        key_resp["string"] = cast_to_type(req[key], str)
        key_resp["numeric"] = cast_to_type(req[key], float)
        key_resp["datetime"] = cast_to_type(req[key], "ms")

        response["data"][key] = key_resp
    
    return jsonify(response)

if __name__ == '__main__': 
    app.run()