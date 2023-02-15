import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = 'https://www.basketball-reference.com/teams/MIL/2023.html'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

data = []
table = soup.find('table', attrs={'class':'stats_table'})
table_head = table.find('thead')
top_row = table_head.find('tr')
cols = top_row.find_all('th')
cols = [ele.text.strip() for ele in cols]
data.append([ele for ele in cols])



table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    headers = row.find_all('th')
    cols = row.find_all('td')
    headers = [ele.text.strip() for ele in headers]
    cols = [ele.text.strip() for ele in cols]
    headers += cols
    data.append([ele for ele in headers ]) # Get rid of empty values
    # data.append([ele for ele in cols]) # Get rid of empty values

print(tabulate(data, headers='firstrow' ,tablefmt='fancy_grid'))

 