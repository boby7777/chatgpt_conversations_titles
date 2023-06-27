import json
from datetime import datetime
from dotenv import load_dotenv
import os

# read settings from .env
load_dotenv()
json_filename = os.getenv("JSON_FILENAME")

# change the path
json_file_path = f"./{json_filename}"

# read json file
with open(json_file_path) as json_file:
    json_data = json.load(json_file)

def count_titles_per_day(json_data):
    titles_per_day = {}

    for entry in json_data:
        # get timestamp of create_time
        create_time = entry['create_time']
        # cnvert timestamp to date
        date = datetime.fromtimestamp(create_time).date()

        # Check if the date already exists in the dictionary, if not, add it.
        if date not in titles_per_day:
            titles_per_day[date] = 0

        # increase title counts
        titles_per_day[date] += 1

    return titles_per_day

# caculate counts of date
titles_per_day = count_titles_per_day(json_data)

# print date and counts
for date, count in titles_per_day.items():
    print(f"{date}: {count} titles")

    # print title
    index = 1
    for item in json_data:
        title = item['title']
        item_create_time = datetime.fromtimestamp(item['create_time']).date()
        if item_create_time == date:
            print(f"{index}. {title}")
            index = index + 1


# Total
count = len(json_data)
print() # empty line
print(f"Total: {count} titles")