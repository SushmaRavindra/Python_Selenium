# Generators.py
import tracemalloc
from itertools import count
import time

def evens(numbers):
    a = []
    for num in numbers:
        if num % 2 == 0:
            a.append(num)
    return a


def evens(numbers):
    print('Running evens')
    for num in numbers:
        if num % 2 == 0:
            yield num
            print('Running after yield statement')


c = count()

n = evens(c)


def read(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    return contents


def read(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line

tracemalloc.start()
data = read('/home/sandeep/Desktop/Selenium/sample.txt')
print('Memory Usage: ', tracemalloc.get_traced_memory())
tracemalloc.stop()


def tail(filename):
    with open(filename, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line


filename = '/home/sandeep/Desktop/test.log'

def grep(pat, line):
    rows = line.split(',')
    if rows[0] in pat:
        yield rows


for line in tail(filename):
    for l in grep(['IBM', 'AA', 'MSFT', 'GE'], line):
        print(l)

for line in tail(filename):
    rows = line.split(',')
    if float(rows[4]) < 0:
        print(f'{rows[0]:>5} {rows[1]:>5} {float(rows[4]):>5.2f}')
