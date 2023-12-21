import sys
from flask import Flask, render_template
from datetime import datetime

app = Flask('Adam')

@app.route("/")
def start():
    return render_template("strona_startowa_zmienna.html",
                           actual_time=datetime.now(),
                           python_version=sys.version)

app.run()