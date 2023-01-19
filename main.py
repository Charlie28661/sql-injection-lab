from flask import Flask
from flask import request
from flask import render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
@app.route("/login", methods = ['GET', 'POST'])
def login_page():
    connect = sqlite3.connect("datebase.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS datebase (ID text, ACCOUNT text, PASSWORD text)")
    #cursor.execute('INSERT INTO datebase values("1", "admin", "scaict")')
    connect.commit()

    try:
        name = request.values["account"]
        pw = request.values["password"]
    except:
        return render_template("login.html")
    cursor.execute(f"SELECT * FROM datebase WHERE ACCOUNT = '{name}' AND PASSWORD = '{pw}'")

    data = cursor.fetchall()
    if len(data) == 0:
        return render_template("login.html")
    return render_template("flag.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
