# Training.py
import time

i = 10  # Integer

f = 1.2     # Float

b = True    # Boolean

ss = 'Hello'     # String

l = [1, 2, 3]   # List

d = {'a': 1, 'b': 2}        # Dictionary

s = {1, 2, 3}       # Set

t = (1, 2, 3)       #Tuple

# Logging Decorator (Parameterised Decorator)
def logging(msg):
    def log(func):
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return log

# Time Decorator
def _time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Execution Time: ',end-start)
        return result
    return wrapper


# Validating Datatypes of arguments passed to a function
def validate(**tys):
    def decorate(func):
        def wrapper(*args, **kwargs):
            # validate the datatype of the arguments
            _tys = list(tys.values())
            _args = list(args)
            for _arg, _typ in zip(_args, _tys):
                if not isinstance(_arg, _typ):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorate


@validate(a=int, b=int)
def add(a, b):
    return a+b

@validate(a=float, b=int)
def sub(a, b):
    return a-b

@validate(name=str)
def greet(name):
    print(f'Hello {name} welcome to Python!')
