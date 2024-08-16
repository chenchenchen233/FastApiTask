"""
This project provides a server which can automatically encode an URL into a shortened one
and decode the shortened URL back to its original one
"""
from fastapi import FastAPI
import uvicorn

import random
import string

app = FastAPI()

SHORT_LENGTH = 5
ENCODE_MAP = {}
DECODE_MAP = {}


def generate_code() -> string:
    """
    randomly generate a code of short length
    :return: random code
    """
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for i in range(SHORT_LENGTH))
    return code


@app.post("/encode")
async def encode(url: str) -> dict:
    """
    encode url into a shortened one
    :param url: original url
    :return: shorten url
    """
    if url in ENCODE_MAP:
        short_url = ENCODE_MAP[url]
    else:
        code = generate_code()
        while code in DECODE_MAP:
            code = generate_code()
        short_url = f"https://shortlink.net/{code}"
        DECODE_MAP[short_url] = url
        ENCODE_MAP[url] = short_url
    return {"short_url": short_url}


@app.post("/decode")
async def decode(short_url: str) -> dict:
    """
    decodes the shortened url
    :param url:
    :return: the original url
    """
    if short_url in DECODE_MAP:
        return {"original_url": DECODE_MAP[short_url]}
    else:
        return {"error": "the short url can not be found"}

if __name__ == "__main__":
    uvicorn.run("server:app", reload=True)
