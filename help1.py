import datetime as dt
import openpyxl as op
file1=op.load_workbook("U:\\py\\help1.xlsx","rw")
active_sheet=file1.active
row=2
column=2
name=input('Enter the name')
while active_sheet.cell(row,column).value != None:
    if name.upper()==active_sheet.cell(row,column).value.upper():
        active_sheet.cell(row,4)=dt.datetime.now
    row+=1