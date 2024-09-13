import requests, os
import random

def get_comics():
    comics_number = random.randrange(1, 2984, 1)
    site_url = f"https://xkcd.com/{comics_number}/info.0.json"
    site_response = requests.get(site_url)
    site_response.raise_for_status()
    site_json = site_response.json()
    comics_comment = site_json["alt"]
    comics_url = site_json["img"]
    return comics_url, comics_comment