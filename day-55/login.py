

class User:
    def __init__(self) -> None:
        self.name = name
        self.is_logged_in = False

def logging_decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@logging_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Emil")

create_blog_post(new_user)
