import functools

# user = {"username": "joe", "access_level": "guest"}
user = {"username": "joe", "access_level": "admin"}


def get_admin_pass():
    return "1234"


# def secure_get_addmin():
#     if user["access_level"] == "admin":
#         return "1234"


# print(secure_get_addmin())
# print(get_admin_pass())


# second step:
# def secure_function(func):
#     if user["access_level"] == "admin":
#         return func


# get_admin_pass = secure_function(get_admin_pass)

# print(get_admin_pass())

# with the second step we recive a Nontype Error if our acessl leve is not by default 'admin'

# decorator way

# def make_secure(func):
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"{user['username']} don't have permesion of admin "
#     return secure_function


# get_admin_pass = make_secure(get_admin_pass)

# the above line not look coool instead we can use @ which is do the same as above line

# @make_secure
# def get_admin_pass():
#     return "1234"


# print(get_admin_pass())

# the only proble is that right now our get_addmin_pass function name is changed to secure_function
# but we have solution for that just import function.Wraper function to avoid
# print(get_admin_pass.__name__)

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"{user['username']} doesn't have the admin permesion"
    return secure_function


@make_secure
def get_admin_pass():
    return "1234"


print(get_admin_pass.__name__)
print(get_admin_pass())


# but again you are lemited with the above function becase it's
# doesn't accept any argument so you have to create *args and **kwargs

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return "user dont have admin permistion"
    return secure_function


@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super secure pass"


print(get_password("billing"))
