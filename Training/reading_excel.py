import xlrd

def read_locators(sheetname):
    wb = xlrd.open_workbook('./Objects.xlsx')
    ws = wb.sheet_by_name(sheetname)
    rows = ws.get_rows()
    headers = next(rows)    # Skip the headers
    data = {row[0].value: (row[1].value, row[2].value) for row in rows}
    return data


wb = xlrd.open_workbook('./Objects.xlsx')
ws = wb.sheet_by_name("RegistrationPage")
print(ws.row_values(4, start_colx=1))


rp = read_locators("RegistrationPage")

lp = read_locators("LoginPage")

print(rp)
print(lp)


def enter_email():
    print(lp['txt_email'])

def enter_password():
    print(lp['txt_password'])

enter_email()
enter_password()