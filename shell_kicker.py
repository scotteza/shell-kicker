from bs4 import BeautifulSoup
import os
import requests

# print("Initialising...")
# os.system('./initialise.sh')
# print("Done initialising")

with open('spreadsheet_id.txt', 'r') as file:
    spreadsheet_id = file.read().strip()

url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/"
# print("Printing URL...")
# print(url)
response = requests.get(url)
if response.status_code != 200:
    print(f"Error, got response code {response.status_code}. Please check your spreadsheet ID. Exiting...")
    quit()

entire_page = BeautifulSoup(response.text, "html.parser")
grid_div = entire_page.find(
    name="div", attrs={"id": "0-grid-table-container"})
if grid_div == None:
    print("Grid div not found. Exiting...")
    quit()

to_search_for = "boot"
found = bool(grid_div.findAll(text=to_search_for))

if found:
    os.system('./found_script.sh')
else:
    os.system('./not_found_script.sh')
