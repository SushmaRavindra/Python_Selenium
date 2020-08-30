import csv
import tracemalloc

filename = '/Users/sandeep/Documents/Python_Selenium/Training/covid_data.csv'


# Making a Tuple
def make_tuple(row):
    return row[2], row[3], int(row[5])


# making a Dictionary
def make_dict(row):
    return {
        "country": row[2],
        "date_": row[3],
        "cases": int(row[5])
    }


# Making a Class Instance
class Covid:
    def __init__(self, row):
        self.country = row[2]
        self.date_ = row[3]
        self.cases = row[5]

getattr()
from collections import namedtuple
Covid = namedtuple('Covid', ['country', 'date_', 'cases'])

from dataclasses import dataclass
@dataclass
class Covid:
    country: str
    date_: str
    cases: str


def memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        print(tracemalloc.get_traced_memory())
        tracemalloc.stop()
        return result

    return wrapper


def _time(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print('Time to Execute: ', stop - start)
        return result

    return wrapper


@_time
def read_csv(filename):
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skipping Headers
        for row in rows:
            records.append(Covid(row))
    return records


data = read_csv(filename)

# All the countries affected by Covid
c = {item.country for item in data}

# Total number of cases in each country
from collections import Counter

c = Counter()

for item in data:
    c[item.country] += int(item.cases)

# 10 Top Countries which has most number of Covid Cases
top_10 = sorted(c.items(), key=lambda item: item[-1])

# Countries with less than 1000 cases
less_1000 = {item.country: item.cases for item in data if int(item.cases) < 1000}

# How many cases were reported on  26/07/2020 in India
dd = Counter()

for item in data:
    dd[(item.country, item.date_)] += int(item.cases)