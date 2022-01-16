import functools

def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request):
            return func(*args, **kwargs)
        else:
            raise Exception("Authentication failed")
    return wrapper

@authenticate
def post_comment(request):
    print('Posting comment successfully')

def check_user_logged_in(request):
    if request is not None:
        return True
    else:
        return False

post_comment("hello")
post_comment(None)