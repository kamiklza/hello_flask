def delay_decorator(function):
    def wrapper_function():
        print(function.__name__)
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")

say_hello()
print(say_hello.__name__)









