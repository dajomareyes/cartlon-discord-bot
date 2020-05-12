import os
import json
import requests
import time
from libs import secrets

ENDPOINT = secrets.get_secret('LAMBDA_ENDPOINT')
ENDPOINT_TOKEN = secrets.get_secret('LAMBDA_TOKEN')

def perform_server_action(action: str):
    headers = {'x-api-key': ENDPOINT_TOKEN}
    data = {'action': action}
    r = requests.get(ENDPOINT, headers=headers, params=data)
    return r.json(), r.status_code

def start_minecraft_server() -> str:
    result = ''
    response, status_code = perform_server_action('start')
    data = response
    if (data['CurrentState']):
        time.sleep(10) # sleep for 10 seconds before getting the status
        result = check_minecraft_server_status()
    return result

def stop_minecraft_server() -> str:
    response, status_code = perform_server_action('stop')
    data = response
    time.sleep(10)
    return data['CurrentState']['Name']

# returns the state of the minecraft server and its IP address
def check_minecraft_server_status() -> str:
    response, status_code = perform_server_action('describe')
    print(response)
    data = response
    # parse server status response and figure out what message to send back to the channel
    if status_code == 200:
        message = '**Server Status:** ```%s``` \n**IP:** ```%s```' % (data['CurrentState']['Name'], data['MinecraftIP'])
    else:
        message = 'Whoops like the Minecraft server isn\'t running'
    return message

