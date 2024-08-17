"""
this is a test file to test the endpoints in server
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server import app

client = TestClient(app)


def test_encode_valid_input():
    response = client.post("/encode", json={"url": "https://codesubmit.io/library/react"})
    assert response.status_code == 200
    assert "short_url" in response.json()


def test_encode_invalid_input():
    ##Test a non-URL input
    response = client.post("/encode", json={"url": "codesubmit.io/library/react"})
    assert response.status_code == 422


def test_decode_valid_input():
    response = client.post("/encode", json={"url": "https://codesubmit.io/library/react"})
    short_url = response.json()["short_url"]
    ## test if it decodes the short URL back to the orginal URL
    response = client.post("/decode", json={"url": short_url})
    assert response.status_code == 200
    assert response.json()["original_url"] == "https://codesubmit.io/library/react"


def test_decode_invalid_input():
    ## test on a short URL which does not exist
    response = client.post("/decode", json={"url": "https://test_short_code.com"})
    assert response.status_code == 200
    assert "error" in response.json()

    ## test on invaLID URL link
    response = client.post("/decode", json={"url": "https/test_short_code.com"})
    assert response.status_code == 422