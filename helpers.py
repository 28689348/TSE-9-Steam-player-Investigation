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
