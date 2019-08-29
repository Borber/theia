import requests
from bs4 import BeautifulSoup


url = "https://www.google.com"
response = requests.get(url).text
soup = BeautifulSoup(response, "lxml")
with open("google.html", "w") as f:
    f.write(soup.prettify())
