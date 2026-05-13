import requests
import csv
from datetime import datetime
import os

url = "https://mobifitness.ru/api/v8/clubs/4573.json"

token = os.environ["API_TOKEN"]

headers = {
    "Authorization": f"Bearer {token}"
}

data = requests.get(url, headers=headers).json()

load = int(data["currentLoad"])

with open("gym.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([datetime.now(), load])

print("Saved:", load)