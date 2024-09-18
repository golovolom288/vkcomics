import os
from dotenv import load_dotenv
import telegram
import random
import shutil
import requests


def get_comics():
    comics_number = random.randrange(1, 2984, 1)
    site_url = f"https://xkcd.com/{comics_number}/info.0.json"
    site_response = requests.get(site_url)
    site_response.raise_for_status()
    site_json = site_response.json()
    comics_comment = site_json["alt"]
    comics_url = site_json["img"]
    return comics_url, comics_comment


def save_img(url, filepath):
    response = requests.get(url)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def send_posts_tg_bot(tg_bot_token, chat_id, alt, directory="comics/"):
    bot = telegram.Bot(token=tg_bot_token)
    photo_path = os.path.join(directory, "comics.jpg")
    with open(photo_path, "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption=alt)


if __name__ == "__main__":
    load_dotenv()
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    chat_id = os.environ["tg_group_id"]
    os.makedirs("comics", exist_ok=True)
    save_img(get_comics()[0], "comics/comics.jpg")
    send_posts_tg_bot(tg_bot_token, chat_id, get_comics()[1], directory="comics/")
    shutil.rmtree("comics")
