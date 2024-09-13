import os
from save_img import save_img
from dotenv import load_dotenv
from tg_bot import send_posts_tg_bot
from get_comics import get_comics


load_dotenv()
tg_bot_token = os.environ["TG_BOT_TOKEN"]
chat_id = os.environ["tg_group_id"]
save_img(get_comics()[0], "comics/comics.jpg")
send_posts_tg_bot(1, tg_bot_token, chat_id, get_comics()[1], directory="comics/")
