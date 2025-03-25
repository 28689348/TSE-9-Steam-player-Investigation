from steam_api import SteamAPI
from helpers import parse_user_info, format_report, parse_friend_count

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

    api = SteamAPI()

    for steam_id in steam_ids:
        print(f"\nFetching data for Steam ID: {steam_id}")
        raw_data = api.get_player_info(steam_id)
        user_info = parse_user_info(raw_data)
        report = format_report(user_info)

        friend_data = api.get_friend_list(steam_id)
        friend_count = parse_friend_count(friend_data)
        
        print(report)
        print(f"Friend Count: {friend_count}\n")

if __name__ == "__main__":
    main()
