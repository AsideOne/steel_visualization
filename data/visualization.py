from flask import Flask, render_template
import sqlite3
import json


app = Flask(__name__)


def fetch_data_for_visualization():
    conn = sqlite3.connect('steel_price.db')
    c = conn.cursor()
    c.execute("SELECT date, price FROM steel_prices")
    rows = c.fetchall()
    conn.close()
    data = []
    for row in rows:
        data.append({'date': row[0], 'price': row[1]})
    return data


@app.route('/')
def index():
    data = fetch_data_for_visualization()
    return render_template('index.html', data=json.dumps(data))


if __name__ == '__main__':
    app.run(debug=True)