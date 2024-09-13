import requests, os


def save_img(url, filepath):
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs("comics", exist_ok=True)
    with open(filepath, 'wb') as file:
        file.write(response.content)





