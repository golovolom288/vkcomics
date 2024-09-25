import os
from dotenv import load_dotenv
import telegram
import random
import shutil
import requests
import pathlib


def get_comics():
    min_index_comics = 1
    max_index_comics = 2984
    comics_number = random.randrange(min_index_comics, max_index_comics, 1)
    site_url = f"https://xkcd.com/{comics_number}/info.0.json"
    site_response = requests.get(site_url)
    site_response.raise_for_status()
    comics = site_response.json()
    comics_comment = comics["alt"]
    comics_url = comics["img"]
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
    comics_url, comics_comment = get_comics()
    load_dotenv()
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    chat_id = os.environ["TG_GROUP_ID"]
    file_path = pathlib.Path.home() / "Desktop" / "python_projects" / "vkcomics" / "comics" / "comics.jpg"
    try:
        os.makedirs("comics", exist_ok=True)
        save_img(comics_url, file_path)
        send_posts_tg_bot(tg_bot_token, chat_id, comics_comment, directory="comics/")
    finally:
        shutil.rmtree("comics")
