from flask import Flask, render_template

app = Flask('Adam')

@app.route("/")
def start():
    return render_template("strona_startowa.html")

app.run()