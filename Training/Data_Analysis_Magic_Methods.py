import csv
from collections import Counter

filename = '/Users/sandeep/Documents/Python_Selenium/Training/covid_data.csv'


class Covid:
    def __init__(self, row):
        self.country = row[2]
        self.date_ = row[3]
        self.cases = int(row[5])


class Data:
    def __init__(self):
        self._records = []

    def __len__(self):
        return len(self._records)

    def __iter__(self):
        return iter(self._records)

    def __getitem__(self, index):
        return self._records[index]

    # Alternate Constructor
    @classmethod
    def from_csv(cls, filepath):
        self = cls()    # Data()
        with open(filepath, 'r') as f:
            rows = csv.reader(f)    # Returns a CSV object
            headers = next(rows)    # Skip Headers
            for row in rows:
                self._records.append(Covid(row))
        return self

    @property
    def countries_affected(self):
        return {item.country for item in self._records}

    @property
    def total_case_country(self):
        c = Counter()
        for item in self._records:
            c[item.country] += item.cases
        return c

    @property
    def cases_by_date(self):
        dd = Counter()
        for item in self._records:
            dd[(item.country, item.date_)] += item.cases
        return dd

    def less_than_1000(self):
        total_cases = self.total_case_country
        return {country: cases for country, cases in total_cases.items() if int(cases) < 1000}

d = Data.from_csv(filename)