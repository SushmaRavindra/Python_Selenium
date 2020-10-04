import xlrd


wb = xlrd.open_workbook('./sample.xlsx')
ws = wb.sheet_by_name('Covid')
rows = ws.get_rows()

for row in rows:
    print(row)
