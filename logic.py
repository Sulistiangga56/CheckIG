import json

def parse_followers(file):
    data = json.load(file)
    followers = [item["value"] for entry in data for item in entry["string_list_data"]]
    return followers

def parse_following(file):
    data = json.load(file)
    following = [item["value"] for entry in data["relationships_following"] for item in entry["string_list_data"]]
    return following

def get_non_followers(followers, following):
    return [user for user in following if user not in followers]
