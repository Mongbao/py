from openpyxl import Workbook
import time

wb=Workbook()
sheet=wb.active

sheet['A1']=2020
sheet['A2']="hello"
sheet['A3']=41.80
sheet['A4']=10

now=time.strftime("%x")
sheet['A5']=now

wb.save("demo.xlsx")
print("End")