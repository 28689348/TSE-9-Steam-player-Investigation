import os
import requests
from dotenv import load_dotenv
from helpers import parse_user_info

# Load environment variables from .env
load_dotenv()

# Get Steam API key from .env
STEAM_API_KEY = os.getenv("STEAM_API_KEY")
if not STEAM_API_KEY:
    print("Error: STEAM_API_KEY not found in .env file.")
    exit(1)

# Define the base URL for the Steam API
BASE_URL = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/"

def get_user_info(steam_id):
    # Prepare the request parameters
    params = {
        "key": STEAM_API_KEY,
        "steamids": steam_id
    }
    # Make a GET request to the Steam API
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()  
    else:
        print(f"Error fetching data for Steam ID {steam_id}.")
        return None

def read_steam_ids(file_path="steam_ids.txt"):
    # Read Steam IDs from the file one per line
    try:
        with open(file_path, "r") as f:
            ids = [line.strip() for line in f if line.strip()]
        return ids
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def main():
    steam_ids = read_steam_ids()
    if not steam_ids:
        print("No Steam IDs to process.")
        return

    for steam_id in steam_ids:
        print(f"\nFetching data for Steam ID: {steam_id}")
        raw_data = get_user_info(steam_id)
        if raw_data:
            user_info = parse_user_info(raw_data)
            if user_info:
                print("User Info:")
                print(f"Name: {user_info['personaname']}")
                print(f"Steam ID: {user_info['steam_id']}")
                print(f"Account Created: {user_info['creation_date']}")
            else:
                print("No user data found.")
        else:
            print("No user info found.")

if __name__ == "__main__":
    main()
