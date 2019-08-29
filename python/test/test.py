import requests


url = "https://www.google.com"
response = requests.get(url).text

print(response)
