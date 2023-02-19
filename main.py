from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=8000, debug=True)

@app.route('/')
def index():
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
        data.append([ele for ele in headers]) # Get rid of empty values

    table = tabulate(data, headers='firstrow', tablefmt='html')
    return render_template('index.html', data=data, table_class='my-table')
