from flask import Flask, render_template, request
from funkcje_dodatkowe.kody import generate_token
from funkcje_dodatkowe.login_functions import login_ok

app = Flask("moja_apka")


@app.route("/")
def mainpage():
    return render_template('static_html.html')


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

@app.route("/user_template/<user_name>")
def user_page_template(user_name):
    return render_template("user_template.html",
                           username=user_name)

# /test_request?a=3&b=45 HTTP/1.1" 200 -
@app.route("/test_request")
def test_request():
    # print(dir(request))
    print(request.remote_addr)
    print(request.headers)
    print("---------------")
    print(request.args)
    print("---------------")
    print(request.args.to_dict())
    return "NIC w html"


# /login?login=login_name&password=some_pass
@app.route("/login/")
def login():
    login_dict = request.args.to_dict()
    if login_ok(login_dict):
        user_login = login_dict['login']
        password = login_dict['password']
        return render_template("login_ok.html",
                               login=user_login,
                               passwd=password)
    else:
        return render_template("login_error.html")

app.run()