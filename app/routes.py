import os
import requests

from app import app
from dotenv import load_dotenv

load_dotenv()

REMOTE_ENTITY = os.getenv('REMOTE_ENTITY')
REMOTE_BASE_URL = os.getenv('REMOTE_BASE_URL')
REMOTE_DEFAULT_OBJECT_ID = os.getenv('REMOTE_DEFAULT_OBJECT_ID')


def fetch_remote_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.RequestException as e:
        return {"error_message": str(e)}, response.status_code


@app.route('/')
@app.route('/index')
def index():
    url = f"{REMOTE_BASE_URL}/{REMOTE_DEFAULT_OBJECT_ID}"
    remote_data, status_code = fetch_remote_data(url)
    result = {
        "remote_entity": REMOTE_ENTITY,
        "remote_endpoint_url": url,
        "status_code": status_code,
        "result": remote_data
    }
    return result, status_code


@app.route('/object/<id>')
def about_object(id):
    url = f"{REMOTE_BASE_URL}/{id}"
    remote_data, status_code = fetch_remote_data(url)
    result = {
        "remote_entity": REMOTE_ENTITY,
        "remote_endpoint_url": url,
        "status_code": status_code,
        "result": remote_data
    }
    return result, status_code
