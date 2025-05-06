import os
import json
from datetime import date

# Create logs folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

def _get_filename_for_date(year, month, day):
    return os.path.join("logs", f"{year:04d}-{month:02d}-{day:02d}.json")

def save_today_data(data):
    today = date.today()
    filename = _get_filename_for_date(today.year, today.month, today.day)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def load_today_data():
    today = date.today()
    filename = _get_filename_for_date(today.year, today.month, today.day)
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def load_data_for_date(year, month, day):
    filename = _get_filename_for_date(year, month, day)
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    return []
