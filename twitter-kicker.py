from bs4 import BeautifulSoup
import os
import requests

page = requests.get("https://twitter.com/bob/with_replies")
something = BeautifulSoup(page.text, "html.parser")
something.find_all(name="div", attrs={"class":"jobsearch-SerpJobCard"})

print(something)

# os.system('ls -l')

