import xlrd
import csv

# Reading Objects.
wb = xlrd.open_workbook("/Users/sandeep/Documents/Demo/Data/Objects.xlsx")
ws = wb.sheet_by_name("HomePage")
rows = ws.get_rows()
headers = next(rows)    # Skipping Headers
d = {row[0].value: (row[1].value, row[2].value) for row in rows}
print(d)


# Reading TestData
wb = xlrd.open_workbook("/Users/sandeep/Documents/Demo/Data/TestData.xlsx")
ws = wb.sheet_by_name("Registration")
rows = ws.get_rows()

for item in rows:
    for i in item:
        print(i.value, end=',')
    print()

print(ws.row_values(0))


print(ws.row_values(8, start_colx=4))

for index, row in enumerate(rows):
    if not row[0].value == 'test_03':
        continue
    headers = ws.row_values(index-1, start_colx=2)
    print(headers)
    break