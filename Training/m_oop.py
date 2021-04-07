class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._points = (self.a, self.b)
    
    def __len__(self):
        print('__len__')
        return len(self._points)
    
    def __getitem__(self, index):
        print('__getitem__')
        return self._points[index]
    
    def __iter__(self):
        print('__iter__')
        return iter(self._points)

    def __contains__(self, item):
        print("__contains__")
        return item in self._points

    def __add__(self, other):
        return (sum(self._points) , sum(other._points))
    
    def __sub__(self, other):
        return (self._points[0] - self._points[1], other._points[0] - other._points[1])
    
    def __setattr__(self, name, value):
        print('__setattr__')
        if name not in {"a", "b", "_points"}:
            raise AttributeError
        if name in {"a", "b"}:
            if value > 10:
                raise ValueError()
        super().__setattr__(name, value)
    
    def __getattribute__(self, name):
        print('__getattribute__')
        return super().__getattribute__(name)
    
    def __delattr__(self, name):
        print('__delattr__')
        raise AttributeError('Cannot delete attr')


# s = "helloworld"
# temp = []
# for i in range(len(s)-1, -1, -1):
#     print(s[i], end='')

# def convert(any_string):
#     l = []
#     for c in any_string:
#         temp = ord(c)   # Get the ASCII value of the character
#         if temp>= 97 and temp<=122:
#             l.append(chr(temp - 32))
#         elif temp>=65 and temp<=90:
#             l.append(chr(temp+32))
#         else:
#             l.append(c)
#     return ''.join(l)

# print(convert('HeLLo123*(&^ Hello'))

class ReadRandomLine:
	def __init__(self, objfile):
		self._objfile = objfile
	
        def __getitem__(self, index):
		lines = self._objfile.readlines()
                try:
		  return lines[index]
                except IndexError:
                  print('Please check the line number')











# class BankAccount:
#     interest_rate = 0.04
#     def __init__(self, fname, lname, amount):
#         self.fname = fname
#         self.lname = lname
#         self.balance = amount
#         self._transactions = []
#         self._transactions.append(f'******* Initial Deposit Amount ***** {amount}')
    
#     def deposit(self, amount):
#         self.balance += amount
#         self._transactions.append(f'Amount Credited Rs. {amount}')
        
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             self._transactions.append(f'Amount Debited Rs {amount}')
    
#     def statement(self):
#         for line in self._transactions:
#             print(line)
#         print(f'Total Available Balance: {self.balance}')
    
#     def roi(self):
#         print('Rate of Interest: ',self.__class__.interest_rate)
    
#     @staticmethod
#     def get_random_number():
#         print('Getting Random Number')

#     @staticmethod
#     def add(a, b):
#         return a+b


# class SavingsBankAccount(BankAccount):
#     interest_rate = 0.045
#     def withdraw(self, amount):
#         if amount > 10000:
#             raise ValueError('Can not withdraw more than 10000 rs')
#         super().withdraw(amount)

# class SalaryAccount(BankAccount):
#     interest_rate = 0.05
#     def __init__(self, fname, lname, amount=0.00):
#         self._first_time = True
#         self._overdraft = 0.00
#         super().__init__(fname, lname, amount)
    
#     def deposit(self, amount):
#         if self._first_time:
#             self.balance += 1000
#             self._first_time = False
#             self._transactions.append(f'******* Bonus 1000 Deposited *********')
#         super().deposit(amount)
    
#     def overdraft(self, amount):
#         if self._overdraft >= 10000:
#             raise ValueError("Overdraft Amount Exceeded 10K")
#         self._overdraft += amount
#         self._transactions.append(f'****** Overdraft Amount Credited Rs. {amount}')
#         super().deposit(amount)

# class SeniorCitizenAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount > 20000:
#             raise ValueError('Can not withdraw more than 20K')
#         super().withdraw(amount)

# class SukanyaSamrudhiAccount(BankAccount):
#     interest_rate = 0.095
#     def deposit(self, amount):
#         if amount < 1000:
#             raise ValueError
#         super().deposit(amount)
    
#     def withdraw(self, amount):
#         raise Exception('Cannot withdraw Amount from SSA')


# class PenaltyAccount:
#     def withdraw(self, amount):
#         self.balance -= 500
#         super().withdraw(amount)

# class RetairementAccount(PenaltyAccount, BankAccount):
#     pass



# s = SalaryAccount("Sandeep", "Surya", 1000)
# BankAccount.get_random_number()



# class Parent:
#     def spam(self):
#         print("Parent Spam")

# class Child1(Parent):
#     def spam(self):
#         print('Child1 Spam')
#         super().spam()

# class Child2(Parent):
#     def spam(self):
#         print('Child2 Spam')
#         super().spam()

# class Parent2(Parent):
#     def spam(self):
#         print("Parent2 Spam")
#         super().spam()


# class Child3(Child2, Parent2):
#     def spam(self):
#         print('Child3 Spam')
#         super().spam()

# class Point:
#     _count = 0    
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.__class__._count += 1
    
#     def move(self, dx, dy):
#         self.a += dx
#         self.b += dy
# print(Point.__dict__)

# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
    
#     @classmethod
#     def from_string(cls, s):
#         parts = s.split(',')
#         return cls(parts[0], parts[1], parts[2])


# s = "Sandeep, Surya, 1000"
# # e = Employee("Sandeep", "Surya", 1000)

# e1 = Employee.from_string(s)

# print(e1.fname)
# print(e1.lname)
# print(e1.pay)

# p1 = Point(1, 2)
# p2 = Point(1, 2)
# p3 = Point(1, 2)
# p4 = Point(1, 2)

# print(Point._count)

# print(p1.__dict__)
# print(p2.__dict__)

# print(Point.__dict__)


# s = RetairementAccount("Sandeep", "Surya", 50000)



# s.deposit(10000)
# s.statement()
# s.withdraw(5000)
# s.statement()















# # Find the longest non-repeated substring in the below string
# s = "This is a Programming language and Programming is education"

# words = s.split()

# d = { word: len(word)  for word in words if words.count(word) == 1}


# s = sorted(d.items(), key=lambda item: item[-1])[-1]

# print(s)



# s1 = "Hello world welcome to python"
# s2 = "Hi how are you welcome to python"

# o_s1 = s1.split()[1::2]
# e_s2 = s2.split()[::2]

# print(o_s1)
# print(e_s2)

# t1 = ' '.join(o_s1)
# t2  = ' '.join(e_s2)

# print(t1 + t2)
# e1 = {"fname": "steve", "lname": "jobs", "pay": 1000}
# e2 = {"fname": "bill", "lname": "gates", "pay": 2000}

# class Spam:
#     pass

# s1 = Spam()
# s2 = Spam()

# print(s1.__dict__)
# print(s2.__dict__)
# class Player:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.health = 100

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy

#     def attack(self, pts):
#         self.health -= pts

# p1 = Player(1, 2)
# p2 = Player(3, 4)
# p3 = Player(5, 6)

# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)

# p1.attack(20)
# p2.attack(50)
# p3.attack(90)

# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)
# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def move(self, dx, dy):
#         self.a += dx
#         self.b += dy


# p1 = Point(1, 2)
# p2 = Point(10, 20)

# print(p1.__dict__)
# print(p2.__dict__)

# # Point.move(p1, 1, 2)
# # Point.move(p2, 1, 2)
# p1.move(1, 2)
# p2.move(10, 20)

# print(p1.__dict__)
# print(p2.__dict__)

# print(p1.a)
# print(p1.b)


# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay

#     def email(self):
#         return f'{self.fname}.{self.lname}@company.com'


#     def pay_hike(self, per_hike):
#         self.pay = self.pay + (self.pay * per_hike)

# e1 = Employee("steve", "jobs", 1000)
# e2 = Employee("bill", "gates", 2000)

# sandeep = Employee('Sandeep', "Surya", 1000)

# print(type(e1))
# print(type(e2))

# print(e1.__dict__)
# print(e2.__dict__)

# e1.pay_hike(0.1)
# e2.pay_hike(0.2)

# print(e1.pay)
# print(e2.pay)

# # print(Employee.email(e1))
# # print(Employee.email(e2))

# print(e1.email())
# print(e2.email())

# print(e1.__dict__)
# print(e2.__dict__)