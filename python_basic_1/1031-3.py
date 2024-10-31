import openpyxl
import os

wb = openpyxl.Workbook()
print(wb.sheetnames)

wb.save(os.path.join(os.getcwd(), "output", "create_workbook.xlsx"))