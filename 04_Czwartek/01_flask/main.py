from flask import Flask

app = Flask("moja_apka")


@app.route("/")
def startowa():
    return '<H1> HEJ! </H1> <a href="witam">Idź do strony.</a>'


@app.route("/witam")
def secondpage():
    html_response = """
    <h2> WITAM! </h2> <hr>
    Tu Adam Jurkiewicz... <br>
    <b> Siemka </b>
    """
    return html_response

app.run()