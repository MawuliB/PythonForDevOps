from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

project_url = os.getenv('ATLASSIAN_URL') + "/project"
issue_url = os.getenv('ATLASSIAN_URL') + "/issue"
API_TOKEN = os.getenv('ATLASSIAN_API_KEY')
MY_EMAIL = os.getenv('MY_EMAIL')


auth = HTTPBasicAuth(MY_EMAIL, API_TOKEN)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/favicon.ico')
def favicon():
    return ''

# create an issue
@app.route('/create', methods=['POST'])
def create():

    payload = request.get_json()

    comment: str = payload["comment"]['body']
    if comment.upper() == "/JIRA":
        title = payload["issue"]["title"]
        description = f'{payload["issue"]["body"]}\n\nBy: {payload["issue"]["user"]["login"]}\n\nLink: {payload["issue"]["html_url"]}'

        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        payload = json.dumps( {
        "fields": {
            "description": {
            "content": [
                {
                "content": [
                    {
                    "text": description,
                    "type": "text"
                    }
                ],
                "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
            },
            "issuetype": {
            "id": "10012"
            },
            "project": {
            "key": "DEV"
            },
            "summary": title,
        },
        "update": {}
        } )

        response = requests.request(
        "POST",
        issue_url,
        data=payload,
        headers=headers,
        auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        return "Just a comment"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)