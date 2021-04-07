### Reading Excel using xlrd

**Installation**

```python
pip3 install xlrd
```
**Sample Excel**
* ![Covid_Sheet](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/Covid.png)
![Stocks_Sheet](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/Stocks.png)

**Create an instance of workbook object.**
```python
import xlrd

wb = xlrd.open_workbook('sample.xlsx')
```

**Create an instance of worksheet object and provide the worksheet name from where the data to be read.**
```python
ws = wb.sheet_by_name('Covid')    # Read all the rows from sheet Covid
```

**get_rows method on worksheet object returns a generator object**
```python
rows = ws.get_rows()

print(rows)

<generator object Sheet.get_rows.<locals>.<genexpr> at 0x7fd612c29660>
```

**Loop through the generator object.**
```python
# Each row in the excel sheet is being represented as a python list.
# Each item of the list is of type "Cell"

for row in rows:
    print(row)

[text:'Country', text:'Date', text:'Cases', text:'Per_Million']
[text:'India', xldate:43947.0, number:26496.0, number:19.2]
[text:'USA', xldate:43948.0, number:39053.0, number:2836.95]
[text:'China', xldate:43949.0, number:83909.0, number:58.29]
[text:'Australia', xldate:43947.0, number:6703.0, number:262.86]
[text:'Japan', xldate:43947.0, number:13182.0, number:104.22]
[text:'France', xldate:43946.0, number:20763.0, number:1901.4]
[text:'Spain', xldate:43947.0, number:15417.0, number:1840.15]
[text:'Germany', xldate:43945.0, number:19535.0, number:3230.98]
[text:'Italy', xldate:43944.0, number:93234.0, number:3230.98]
```

**To get the actual value of the cell in string format.** 
```python
for row in rows:
    print(row[0].value, row[1].value, row[2].value)

Country Cases Per_Million
India 26496.0 19.2
USA 39053.0 2836.95
China 83909.0 58.29
Australia 6703.0 262.86
Japan 13182.0 104.22
France 20763.0 1901.4
Spain 15417.0 1840.15
Germany 19535.0 3230.98
Italy 93234.0 3230.98
```

**Since rows is a generator object you can feed that object to next() function.**

```python
import xlrd

wb = xlrd.open_workbook('./sample.xlsx')
ws = wb.sheet_by_name('Covid')
rows = ws.get_rows()

headers = next(rows)

print(headers[0].value, headers[1].value, headers[2].value)

Country Cases Per_Million
```

**Reading Objects into Python Dictionary**
```python
def read_locators(sheetname):
    workbook = xlrd.open_workbook("Objects.xlsx")
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    headers = next(rows)     
    return {item[0].value: (item[1].value, item[2].value) for row in rows}

objects = read_locators('LoginPage')

print(objects)

{'txt_email': ('name', 'Email'), 'txt_password': ('name', 'Password'), 'btn_login': ('xpath', "//input[@value='Log in']")}
```
**Reading Testdata**
```python
def read_data(sheetname, testcase):
    workbook = xlrd.open_workbook("TestData.xlsx")
    worksheet = workbook.sheet_by_name(sheetname)
    data = []
    headers = None
    rows = worksheet.get_rows()
    for rowno, row in enumerate(rows):
        if row[0].value == testcase:
            headers = worksheet.row_values(rowno - 1, start_colx=2)
            headers = [item for item in headers if item]
            headers = ','.join(headers)
            break

    rows = worksheet.get_rows()  # Re-initialising iterator

    for rowno, row in enumerate(rows):
        if row[0].value == testcase:
            # Get the row values of the existing row from column-1
            temp_data = worksheet.row_values(rowno, start_colx=1)
            temp_data = [item for item in temp_data if item]
            # Append the list only if the execute column is "Yes"
            if temp_data[0].lower() == "yes":
                data.append(tuple(temp_data[1:]))
    return [headers, data]
```


