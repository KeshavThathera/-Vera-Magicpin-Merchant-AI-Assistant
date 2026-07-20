import urllib.request
import json
import sys

URLS = [
   "https://vera-magicpin-merchant-ai-assistant.onrender.com/v1/healthz",
"https://vera-magicpin-merchant-ai-assistant.onrender.com/v1/metadata"
]

for url in URLS:
    try:
        print(f"Testing {url}...")
        resp = urllib.request.urlopen(url, timeout=15)
        print(f"Status: {resp.getcode()}")
        print(f"Body: {resp.read().decode()}")
    except Exception as e:
        print(f"Error at {url}: {e}")
