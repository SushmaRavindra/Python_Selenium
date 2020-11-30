import time


def add(a, b):
    print(a+b)


def greet(name):
    print('hello {}'.format(name))


def delay(x, _delay, *args, **kwargs):
    print(args)
    time.sleep(_delay)
    x(*args, **kwargs)  # add(1, 2)  greet("Sandeep")

# def delay(func1, func2, _delay, *args):
#     time.sleep(_delay)
#     func1(*args)       # add(1, 2, "Sandeep")
#     func2(*args)        # greet(1, 2, "Sandeep")


delay(x=add, _delay=3, a=1, b=2)
delay(x=add, _delay=3)


# from itertools import count
# from collections import defaultdict
# # d = defaultdict(list)
# #
# # sentence = "python is a programming language"
# #
# # words = sentence.split()
# #
# # for word in words:
# #     d[word[0]].append(word)
# #
# # print(d)
# #
# # nd = {}
# #
# # for word in words:
# #     if word[0] in nd:
# #         nd[word[0]].append(word)
# #     else:
# #         nd[word[0]] = [word]
# #
# # print(nd)
#
# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
#
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
#
#
#
# # def convert(any_string):
# #     l = []
# #     for c in any_string:
# #         temp = ord(c)   # Get the ASCII value of the character
# #         if temp>= 97 and temp<=122:
# #             l.append(chr(temp - 32))
# #         elif temp>=65 and temp<=90:
# #             l.append(chr(temp+32))
# #     return ''.join(l)
# #
# # print(convert('Hello WorlD'))
# # l = ['h', 'i', 'hello', 'how', 'a', 'r', 'e', 'you']
# #
# # s = ''
# #
# # for item in l:
# #     if len(item) == 1:
# #         s = s + item
# #     else:
# #         s = s + ' '+item+' '
# #
# # print(s.split())
#
# #
# # class BankAccount:
# #     c = count(start=1)
# #     _accounts = []  # List to keep track of all the accounts
# #     interest_rate = 4.0
# #
# #     def __init__(self, fname, lname, amount):
# #         self.fname = fname
# #         self.lname = lname
# #         self.amount = float(amount)
# #         self._open_account()
# #
# #     def _open_account(self):
# #         BankAccount._accounts.append(
# #             {"fname": self.fname,
# #              "lname": self.lname,
# #              "amount": self.amount,
# #              "account_no": str(next(self.c)).zfill(9)
# #              })
# #
# #     def deposit(self, amount):
# #         self.amount += float(amount)
# #
# #     def withdraw(self, amount):
# #         if amount <= self.amount:
# #             self.amount -= amount
# #
# #     def statement(self):
# #         print(f"Available Account Balance: {self.amount}")
# #
# #     # Interest Credited every month
# #     def roi(self):
# #         self.amount = self.amount + self.amount * (self.interest_rate / 100)
# #
# #     def close_account(self):
# #         del self
# #
# #     def __del__(self):
# #         print('Deleted')
# #
# #
# # class SavingsAccount(BankAccount):
# #     interest_rate = 4.0
# #
# #     def withdraw(self, amount):
# #         if amount > 10000:
# #             raise ValueError('Can not withdrwa more than 10000 per day')
# #         super().withdraw(amount)
# #
# #
# # class SalaryAccount(BankAccount):
# #     pass
# #
# #
# # class SeniorCitizenAccount(BankAccount):
# #     interest_rate = 5.5
# #
# #     def withdraw(self, amount):
# #         if amount > 20000:
# #             raise ValueError('Can not withdrwa more than 20000 per day')
# #         super().withdraw(amount)
# #
# #
# # class SukanyaSamrudhiAccount(BankAccount):
# #     interest_rate = 9.5
# #
# #     def deposit(self, amount):
# #         if amount < 1000:
# #             raise ValueError('Min Amount Should be 1000rs')
# #         super().deposit(amount)
# #
# #     # Completely overriding the parent class method "withdraw"
# #     def withdraw(self, amount):
# #         raise Exception("Can not withdraw")
# #
# #
# # s1 = SavingsAccount("Sandeep", "Suryaprasad", 2000)
# # s2 = SavingsAccount("Sandeep", "Suryaprasad", 2000)
# # s3 = SukanyaSamrudhiAccount("Sthuthi", "Sandeep", 10000)
# #
# # s1.close_account()