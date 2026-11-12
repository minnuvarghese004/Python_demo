#openpyxl is a python library used to work with excel spreadsheets
# 1.Create new excel file
# 2.Read existing file
# 3.Write data into cells
# 4.Delete Rows and columns
# 5.Work with multiple sheets

#How to install : python -m pip install openpyxl
import openpyxl
#Reading an existing excel file
workbook = openpyxl.load_workbook("C:\\Users\\Minnu\\Downloads\\student_data.xlsx")
sheet = workbook["Data"]
print(sheet["A2"].value)
print(sheet["D2"].value)

#Reading all rows from an excel
for row in sheet.iter_rows(values_only=True):
    print(row)

print(sheet.max_row)
print(sheet.max_column)


