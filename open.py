<<<<<<< HEAD
from openpyxl import Workbook
import time

wb=Workbook()
sheet=wb.active

sheet['A1']=2020
sheet['A2']='hello'
sheet['A3']=41.89
sheet['A4']=10

now=time.strftime("%x")
sheet['A5']=now

wb.save("demo.xlsx")
print('End')
=======
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
>>>>>>> fe9e2dd1896dc4ab817a792b633e8329919aee2a
