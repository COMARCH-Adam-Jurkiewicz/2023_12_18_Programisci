from flask import Flask, request, render_template
from datetime import datetime

app = Flask('Adam')

@app.route("/")
def start():
    return render_template("strona_startowa_zmienna.html",
                           actual_time=datetime.now())

@app.route('/sprawdzam', methods=['GET'])
def form_get():
    return render_template("form_check.html")

@app.route('/sprawdzam', methods=['POST'])
def form_post():
    web = request.form['web']
    return f'Witaj! Twoja strona do sprawwdzenia to {web}.'




app.run()