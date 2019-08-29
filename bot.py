import os
import time
import re
from slackclient import SlackClient
import requests
import dotenv
from flask import Flask, jsonify, request

dotenv.load_dotenv()
token = os.getenv("SLACK_TOKEN")

app = Flask(__name__)

@app.route('/doggo', methods=['POST'])
def doggo():
    if request.form['token'] == token:
        if request.form['text'] == "cat":
            r = requests.get('https://aws.random.cat/meow')
            json = r.json()
            payload = {'response_type':'in_channel', 'text': json["file"]}
            return jsonify(payload)
        elif request.form['text'] == "dog":
            r = requests.get('https://random.dog/woof.json')
            json = r.json()
            payload = {'response_type':'in_channel', 'text': json["url"]}
            return jsonify(payload)
        elif request.form['text'] == "fox":
            r = requests.get('https://randomfox.ca/floof/')
            json = r.json()
            payload = {'response_type':'in_channel', 'text': json["image"]}
            return jsonify(payload)
        else:
            payload = {'text':'oof'}
            return jsonify(payload)
    else:
        payload = {'text':'oof'}
        return jsonify(payload)

if __name__ == "__main__":
    app.run()