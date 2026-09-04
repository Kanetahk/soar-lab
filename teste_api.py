import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"Bearer {token}"}
response = requests.get("https://api.github.com/rate_limit", headers=headers)
print(response.status_code)
print(response.json())