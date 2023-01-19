from flask import Flask
from flask import request
from flask import render_template
import sqlite3

app = Flask(__name__)

connect = sqlite3.connect("datebase.db")
cursor = connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS datebase (id text, account text, password text)")
#cursor.execute('INSERT INTO datebase values("1", "admin", "@@@@@@@@")')
connect.commit()
date = cursor.execute('SELECT * FROM datebase')
check = date.fetchone()


@app.route("/")
@app.route("/login", methods = ['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        name = request.values["account"]
        pw = request.values["password"]
        if name == check[1] and pw == check[2]:
            return render_template("flag.html")
        else:
            return render_template("login.html")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
