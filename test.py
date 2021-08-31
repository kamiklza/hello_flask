# def delay_decorator(function):
#     def wrapper_function():
#         function()
#         function()
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# say_hello()
# print(say_hello.__name__)


class User:
    def __init__(self, name, level):
        self.name = name
        self.is_logged_in = False
        self.level = level

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        function(args[0], kwargs["level"])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user, level):
    print(f"This is {user.name}'s new blog post. He is a {level} user.")

new_user = User("Ken", level="vip")
create_blog_post(new_user, level=new_user.level)









