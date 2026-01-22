# neynar-simple-cast-poster.py
# Wymaga: pip install requests python-dotenv

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEYNAR_API_KEY")
SIGNER_UUID = os.getenv("SIGNER_UUID")  # twój signer z Neynar

def post_cast(text: str, parent_url: str = None):
    url = "https://api.neynar.com/v2/farcaster/cast"
    headers = {"api_key": API_KEY}
    payload = {
        "signer_uuid": SIGNER_UUID,
        "text": text[:280],
    }
    if parent_url:
        payload["parent_url"] = parent_url

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Cast posted!", response.json()["cast"]["hash"])
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    text = input("Cast text: ")
    parent = input("Parent cast URL (optional): ") or None
    post_cast(text, parent)
