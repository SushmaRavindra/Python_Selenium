import xlrd


def read_locators(sheetname):
    workbook = xlrd.open_workbook("Objects.xlsx")
    worksheet = workbook.sheet_by_name(sheetname)
    r = worksheet.get_rows()
    next(r)     # Skip Headers
    return {item[0].value: (item[1].value, item[2].value) for item in r}


objects = read_locators("LoginPage")

print(objects)
