import requests
from libs import secrets

GIPHY_TOKEN = secrets.get_secret('GIPHY_TOKEN')
SEARCH = 'https://api.giphy.com/v1/gifs/search'

def get_first_gif(query):
    data = {
        'api_key': GIPHY_TOKEN,
        'q': query,
        'limit': 1
        }
    response = requests.get(SEARCH, params=data)
    data = response.json()['data']
    # get the bitly url to pass into the discord
    if len(data) > 0:
        image_url = data[0]['bitly_url']
    else:
        image_url = ''
    print(image_url)
    return image_url

# TODO: Create a randomize method that selects a different image everytime instead of the same image