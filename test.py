"""
this is a test file to test the endpoints in server
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server import app

client = TestClient(app)

def test_encode():
    response = client.post("/encode", json={"url": "https://codesubmit.io/library/react"})
    assert response.status_code == 200
    assert "short_url" in response.json()

def test_decode():
    response = client.post("/encode", json={"url": "https://codesubmit.io/library/react"})
    short_url = response.json()["short_url"]

    response = client.post("/decode", json={"short_url": short_url})
    assert response.status_code == 200
    assert response.json()["original_url"] == "https://codesubmit.io/library/react"

import requests
test_encode()
url ='https://codesubmit.io/library/react'
response = client.get("/test")
x = client.post("/encode", json={'url': url})
print(x)
