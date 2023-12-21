from flask import Flask, request, render_template
from datetime import datetime

app = Flask('Adam')

@app.route("/")
def start():
    return render_template("strona_startowa_zmienna.html",
                           actual_time=datetime.now())

@app.route('/sprawdzam', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template("form_check.html")

    if request.method == 'POST':
        web = request.form['web']
        return f'Witaj! Twoja strona do sprawwdzenia to {web}.'

    return "To nie powinno się wyświetlić!"


app.run()