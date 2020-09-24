import xlrd
import csv

# Reading Objects.
wb = xlrd.open_workbook("/Users/sandeep/Documents/Demo/Data/Objects.xlsx")
ws = wb.sheet_by_name("RegistrationPage")
rows = ws.get_rows()
headers = next(rows)    # Skipping Headers
d = {row[0].value: (row[1].value, row[2].value) for row in rows}
print(d)
