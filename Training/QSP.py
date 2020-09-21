# Logging Decorator
def log(func):
    def wrapper(*args, **kwargs):
        print('You called ', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log
def greet():
    return 'Hello'

# a = log(greet)
# a()


@log
def greeting():
    return 'Welcome to Python'


@log
def spam():
    return 'Running Spam'


@log
def demo():
    return "Hello", "Welcome to Python", "Running Spam"


@log
def add(a, b):
    return a+b


@log
def mul(a, b):
    return a*b


@log
def wow(name, *, age):
    print(name, age)


# wow('Sandeep', age=26)
# print(add(1, 2))

# print(mul(2, 3))
# a = log(add)
# print(a(1, 2))

# add(1, 2)

