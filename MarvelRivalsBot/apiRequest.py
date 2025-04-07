import requests
import json
from dotenv import load_dotenv
import os
import time

load_dotenv()

def get_UID(username, api_key):
    url = f'https://marvelrivalsapi.com/api/v1/find-player/{username}'
    headers = {'x-api-key': api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Will raise an exception for 4XX/5XX status
        data = response.json()
        if 'uid' in data:
            return data['uid']
        else:
            print("UID not found in the response")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error getting UID: {str(e)}")

def update_player_data(uid, api_key):
    url = f'https://marvelrivalsapi.com/api/v1/player/{uid}/update'
    headers = {'x-api-key': api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Will raise an exception for 4XX/5XX status
        print("Update :", response.json())
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error updating player data: {str(e)}")
        if hasattr(e, 'response') and e.response:
            print(f"Status code: {e.response.status_code}")
            try:
                print(f"Response: {e.response.json()}")
            except:
                print(f"Response text: {e.response.text}")
        return False

def get_player_data(player_name, api_key):
    uid = get_UID(player_name, api_key)
    if not update_player_data(uid, api_key):
        print("Warning: Player data update failed, trying to get cached data")
    
    time.sleep(1)
    
    url = f"https://marvelrivalsapi.com/api/v1/player/{uid}?season=2"

    headers = {"x-api-key": api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting player data: {str(e)}")
        if hasattr(e, 'response') and e.response:
            print(f"Status code: {e.response.status_code}")
        return None

player_name = "stully18"
api_key = os.getenv("MARVEL_RIVALS_API_KEY")

if not api_key:
    print("API key not found. Please check your .env file")
    exit(1)

player_data = get_player_data(player_name, api_key)

if player_data:
    print(json.dumps(player_data, indent=4))
else:
    print("Failed to retrieve player data")