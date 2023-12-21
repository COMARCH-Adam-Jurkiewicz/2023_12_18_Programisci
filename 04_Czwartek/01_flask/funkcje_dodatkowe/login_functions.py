def login_ok(dictonary):
    """
    web request -> ?login=login_name&password=some_pass
    :param dictonary: {'login': "login_name", 'password': "hasełko" }
    :return:
    """
    if not isinstance(dictonary, dict):
        return False
    if not 'login' in dictonary:
        return False
    if not 'password' in dictonary:
        return False

    # dobry login
    if dictonary['login'] == "logowanie" and dictonary['password'] == "tajnie":
        return True
