import json
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
import os

# read settings from .env
load_dotenv()
json_filename = os.getenv("JSON_FILENAME")

# change the path
json_file_path = f"./{json_filename}"

# read json file and load into pandas DataFrame
with open(json_file_path) as json_file:
    json_data = json.load(json_file)
    df = pd.DataFrame(json_data)

# convert timestamps to dates
df['date'] = pd.to_datetime(df['create_time'], unit='s').dt.date

# Drop all columns except 'title' and 'date'
df = df[['title', 'date']]

# Write DataFrame to Excel file
output_filename = "output.xlsx"
df.to_excel(output_filename, index=False, engine='openpyxl')
print(f"Excel file saved as {output_filename}")
