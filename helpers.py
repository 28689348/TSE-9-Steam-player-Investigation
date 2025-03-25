from datetime import datetime

'''
helpers.py contains functions to process and format the raw data from API.
'''

def unix_to_date(timestamp):
#Convert a Unix timestamp to a simple date string.
    try:
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    except Exception:
        return "N/A"

def parse_user_info(raw_data):
# Tries to retrieve the list of players from the raw_data.
    players = raw_data.get("response", {}).get("players", [])
    if not players:
        return None
    player = players[0]
    return {
        "steam_id": player.get("steamid", "Unknown"),
        "personaname": player.get("personaname", "Unknown"),
        "creation_date": unix_to_date(player.get("timecreated", 0))
    }

def format_report(user_info):
# Returns a formatted report string for the given user info
    if not user_info:
        return "No user data available."
    report = (
        f"User Report:\n"
        f"Name: {user_info.get('personaname')}\n"
        f"Steam ID: {user_info.get('steam_id')}\n"
        f"Account Created: {user_info.get('creation_date')}\n"
    )
    return report

def parse_friend_count(raw_data):
# Extract the number of friends from the raw friend list API response
    friends = raw_data.get("friendslist", {}).get("friends", [])
    return len(friends) if friends else 0
