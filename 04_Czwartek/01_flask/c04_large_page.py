from flask import Flask
from yourapplication import views

app = Flask("apka")
app.add_url_rule('/1', view_func=views.fn1)
app.add_url_rule('/2', methods=['POST'], view_func=views.fn2)

@app.route("/")
def start():
    return "Main page"

app.run(debug=True)