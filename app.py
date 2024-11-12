import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_cafes():
    conn = sqlite3.connect('cafes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, has_wifi, has_sockets FROM cafe WHERE has_wifi = 1 AND has_sockets = 1")
    cafes = cursor.fetchall()
    conn.close()
    return cafes

@app.route('/')
def index():
    cafes = get_cafes()
    return render_template('cafe_list.html', cafes=cafes)

if __name__ == '__main__':
    app.run(debug=True)