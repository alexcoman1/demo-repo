import requests
from bs4 import BeautifulSoup

URL = input("Enter the URL of the page you want to scrape: ")
TAG = input("Enter the HTML tag you want to search for: ")

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# Find all the TAG tags on the page
tags = soup.find_all(TAG)

# Print the contents of each TAG tag
for tag in tags:
  print(tag.text)
