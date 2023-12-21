from flask import Flask
from funkcje_dodatkowe.kody import generate_token

app = Flask("moja_apka")


@app.route("/")
def mainpage():
    return '<H1> HEJ! </H1> <a href="witam">Idź do strony.</a>'


@app.route("/witam")
def secondpage():
    new_token = generate_token()
    html_response = f"""
    <h2> WITAM! </h2> <hr>
    Tu Adam Jurkiewicz... <br>
    <b> Siemka - {new_token}</b> <br>
    <h4><a href="/user/{new_token}">Idź do strony usera - {new_token}.</a></h4>
    """
    return html_response


@app.route("/user/")
def user_info():
    html = """
    Podaj po znaku / swój login, np.: /user/adasiek"""
    return html


@app.route("/user/<user_name>")
def user_page(user_name):
    html = f"""
        <H1>Welcome new user</H1>
        Wysyłam ci maila na adres: {user_name}
        """
    return html


app.run()