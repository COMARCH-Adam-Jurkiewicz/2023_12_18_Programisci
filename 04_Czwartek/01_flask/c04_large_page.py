import sys
import subprocess
from flask import Flask, request, render_template
from datetime import datetime
from yourapplication import views


app = Flask("apka")
app.add_url_rule('/1', view_func=views.fn1)
app.add_url_rule('/2', methods=['POST'], view_func=views.fn2)

@app.route("/")
def start():
    return "Main page"

@app.route("/parametr/<username>")
def get_params(username):
    return f"Podano parametr: {username} "


@app.route("/parametr/<username>/status")
def status(username):
    return f"Sprawdzam status: {username} "


@app.route("/parametry")
def parametry():
    remote = request.remote_addr
    lang = request.accept_languages
    headers = request.headers
    params = request.args
    val_params = request.args.to_dict()
    ret_code = "brak IP"
    # oczekujemy /parametry?ip=192.168.1.1
    if "ip" in val_params:
        ip = str(val_params['ip'])
        print(f"{type(ip)} | {ip=}")
        if sys.platform == 'win32':
            command = ["ping", ip]
        else:
            command = ["ping", "-c", "4", ip]
        ret_code = subprocess.run(command, capture_output=True)

    return render_template("parametry.html",
                           time=datetime.now(),
                           remote=remote,
                           lang=lang,
                           params=params,
                           headers=headers,
                           val_params = val_params,
                           wynik=ret_code.stdout.decode()
                           )

app.run(debug=True)