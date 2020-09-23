# Logging Decorator
def log(func):
    def wrapper(*args, **kwargs):
        print('You called ', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    print(a+b)

@log
def sub(a, b):
    print(a-b)

@log
def mul(a, b):
    print(a*b)


# Parameterised Decorator
def logging(msg='You called :', debug=True):
    def log(func):
        def wrapper(*args, **kwargs):
            if debug:       # debug == True
                print(msg, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return log


@logging("hello You called")
def add(a, b):
    print(a+b)


@logging("Hey there you called")
def sub(a, b):
    print(a-b)


@logging("Hello", debug=False)
def mul(a, b):
    print(a*b)


add(1, 2)

mul(2, 3)

import csv
import tracemalloc
from time import sleep


def _time(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Execution Time: {end-start}')
        return result
    return wrapper


# Decorator that measures Memory
def _memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        print(tracemalloc.get_traced_memory())
        tracemalloc.stop()
        return result
    return wrapper


@_memory
@_time
def apple():
    sleep(1)
    print("Apple")


apple()