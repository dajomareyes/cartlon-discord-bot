import os
import requests
from libs import secrets

ENDPOINT = secrets.get_secret('LAMBDA_ENDPOINT')
ENDPOINT_TOKEN = secrets.get_secret('LAMBDA_TOKEN')

def perform_server_action(action):
    headers = {'x-api-key': ENDPOINT_TOKEN}
    data = {'action': action}
    r = requests.get(ENDPOINT, headers=headers, params=data)
    return r.json()

def start_minecraft_server():
    response = perform_server_action('start')
    return response.json()

def stop_minecraft_server():
    response = perform_server_action('stop')
    return response.json()

def check_minecraft_server_status():
    response = perform_server_action('describe')
    # parse server status response and figure out what message to send back to the channel
    return response.json()

