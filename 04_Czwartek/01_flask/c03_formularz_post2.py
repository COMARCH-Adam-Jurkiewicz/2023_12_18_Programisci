import sys
from flask import Flask, request, render_template, redirect
from datetime import datetime
from funkcje_dodatkowe.page_check import check_web_page

app = Flask('Adam')

@app.route("/")
def start():
    return render_template("strona_startowa_zmienna.html",
                           actual_time=datetime.now(),
                           python_version=sys.version)

@app.route('/sprawdzam', methods=['GET'])
def form_get():
    return render_template("form_check.html")

@app.route('/sprawdzam', methods=['POST'])
def form_post():
    web = request.form['web']
    link = check_web_page(web)
    return redirect(link)
        # f'Witaj! Twoja strona do sprawwdzenia to {web} - wynik to {link}.'




app.run()