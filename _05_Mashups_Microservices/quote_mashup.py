import os
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

template = """
    some text
"""


def get_quote():
    response = requests.get("url")
    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all('dt', class_='quote')


def get_image(quote):
    payload = {"key": template.format(quote)}
    response = requests.get('url', params=payload)
    return response.content


@app.route('/')
def home():
    quote = get_quote().strip()
    body = get_image(quote=quote)
    return Response(response=body, mimetype='image/jpeg')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6787))
    app.run(host='0.0.0.0', port=port)
