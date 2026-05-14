import requests
import csv
from datetime import datetime, timedelta, timezone
import os

url = "https://mobifitness.ru/api/v8/clubs/4573.json"

token = os.environ["API_TOKEN"]

headers = {
    "Authorization": f"Bearer {token}"
}

data = requests.get(url, headers=headers).json()

load = int(data["currentLoad"])

moscow_tz = timezone(timedelta(hours=3))
current_time = datetime.now(moscow_tz)

with open("gym.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([current_time, load])

print("Saved:", load)
