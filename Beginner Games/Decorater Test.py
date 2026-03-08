def app_login(func):
    def authentification(*args, **kwargs):
        return func(*args, **kwargs)
    return authentification


@app_login
def check_user_permissions(has_rights=True):
    if has_rights:
        print("Login was successful")
        return True
    else:
        print("Not enough rights to login")
        return False

login_result = check_user_permissions(has_rights=True)