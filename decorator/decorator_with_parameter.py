import functools

user = {"username": "joe", "access_level": "admin"}

# fi you wnat to give acess admin only to admin or user dashboard to only users:
# do this:


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"{user['username']} doesn't have the permesion to this {access_level}"
        return secure_function
    return decorator

# you need to call it ()


@make_secure("admin")
def get_admin_pass():
    return "admin 1234"


@make_secure("guest")
def get_dashboard_pass():
    return "user guest: pass"


print(get_admin_pass())
print(get_dashboard_pass())

user = {"username": "bill", "access_level": "guest"}

print(get_admin_pass())
print(get_dashboard_pass())
