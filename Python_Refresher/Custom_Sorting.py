# SORTING LIST's
from operator import itemgetter

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
sorted_names = sorted(names)    # sorted method returns a new list in sorted order
print('Sorted List', sorted_names)
print('Original List', names)       # Original list remains un-changed

names.sort()    # sort method sorts the original list inplace
print('Sorted List', names)

reverse_names = sorted(names, reverse=True)
print(reverse_names)    # sorts the list in decending order

# ======================================================
# SORTING TUPLES
tup = (1, 2, 5, 3, 9, 8, 6, 7, 0)
# Tuple does not have method .sort() to sort it inplace. So we have to use sorted() method to sort tuple's
sorted_tup = sorted(tup)
print('Sorted Tuple ', sorted_tup)

# Sorting Dictionary

profile = {'fname': 'mark', 'lname': 'rob', 'language': ['java', 'python'], 'salary': 90000, 'age': 30}

sorted_dict = sorted(profile)

print(sorted_dict)      # Sorts the keys of the dictionary in ascending order

temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]

# Prints [('Bangalore', 25), ('Chennai', 37), ('Delhi', 35), ('Mumbai', 32)]
print(sorted(temperatures))

# Prints [('Bangalore', 25), ('Mumbai', 32), ('Delhi', 35), ('Chennai', 37)]
sorted(temperatures, key=lambda item: item[-1])

my_dict = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(my_dict.items(), key=lambda item: item[1]))  # Sorts the values of the dictionary in ascending order

prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
        }

print(sorted(prices.items(), key=lambda d: d[-1]))
min_p, *_, max_p = sorted(prices.items(), key=lambda d: d[-1])

print(min_p)
print(max_p)

# OR

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

# OR

print(sorted(zip(prices.values(), prices.keys())))

# Custom Sorting
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

# Sorting the list based on the number of characters of the list item
print(sorted(names, key=len))

# Sorting the list based on the last character of the list item
print(sorted(names, key=lambda name: name[-1]))

portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(sorted(portfolio, key=lambda d: d.get('name')))  # Sorts on the key 'name'
print(sorted(portfolio, key=lambda d: d.get('shares')))  # Sorts on the key 'shares'
print(sorted(portfolio, key=lambda d: d.get('price')))  # Sorts on the key 'price'

# Sorting using itemgetter
print(sorted(portfolio, key=itemgetter('name')))

print(sorted(portfolio, key=itemgetter('name', 'shares')))

data = [
        {'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'},
        {'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
        {'fname': 'John', 'uid': 1001, 'lname': 'Cleese'},
        {'fname': 'Big', 'uid': 1004, 'lname': 'Jones'},
]

print(sorted(data, key=itemgetter('fname', 'lname')))
print(sorted(data, key=itemgetter('lname', 'fname')))