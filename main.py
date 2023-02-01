import requests
from bs4 import BeautifulSoup

url = 'https://www.basketball-reference.com/teams/MIL/2023.html'
html_text = requests.get(url).text
nba = BeautifulSoup(html_text, 'html.parser')

print(nba.get_text())


 