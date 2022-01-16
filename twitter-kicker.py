from bs4 import BeautifulSoup
import os
import requests

print("Initialising...")
os.system('./initialise.sh')
print("Done initialising")

with open('spreadsheet_id.txt', 'r') as file:
    spreadsheet_id = file.read()

url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/"
page = requests.get(url)
entire_page = BeautifulSoup(page.text, "html.parser")
grid_div = entire_page.find(
    name="div", attrs={"id": "0-grid-table-container"})

to_search_for = "boot"

found = bool(grid_div.findAll(text=to_search_for))

if found:
    os.system('./found_script.sh')
else:
    os.system('./not_found_script.sh')
