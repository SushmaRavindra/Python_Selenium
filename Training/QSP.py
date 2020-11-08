import xlrd

# Creating Object Instance to Workbook Object
wb = xlrd.open_workbook("./sample.xlsx")

# Creating Object Instance to Worksheet Object
ws = wb.sheet_by_name("Stocks")

rows = ws.row_values(rowx=3, start_colx=0)

print(rows)