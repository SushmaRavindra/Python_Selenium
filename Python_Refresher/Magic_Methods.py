import csv

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def __str__(self):
        return f'Employee({self.fname} , {self.lname}, {self.pay})'

    def __add__(self, other):
        return self.pay + other.pay

    def __sub__(self, other):
        return self.pay - other.pay

    def __mul__(self, other):
        return self.pay * other.pay

    def __gt__(self, other):
        return self.pay > other.pay

    def __lt__(self, other):
        return self.pay < other.pay


class Developers:
    def __init__(self):
        self._developers = []

    @classmethod
    def from_csv(cls):
        d = cls()
        with open('/home/sandeep/Desktop/Selenium/emp.csv') as f:
            rows = csv.reader(f)
            headers = next(rows)  # Skipping headers
            for row in rows:
                e = Employee(row[0], row[1], row[2])
                d._developers.append(e)
        return d

    def __len__(self):
        return len(self._developers)

    def __iter__(self):
        return iter(self._developers)

    def __getitem__(self, name):
        return self._developers[name]

    def __setitem__(self, name, value):
        self._developers[name] = value


d = Developers.from_csv()
