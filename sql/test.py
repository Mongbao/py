import pymssql

#server 資料庫伺服器名稱或IP    (192.168.0.30\SQLEXPRESS)
#user   使用者名稱             (sa)
#password   密碼               (sa)
#database   資料庫名稱          (Northwind)
#conn = pymssql.connect(server,user,userpassword,database)

conn = pymssql.connect(
    host='192.168.0.30\SQLEXPRESS',
    user='sa',
    password='sa',
    database='Northwind')
#if connect:
#    print("連線成功")
cursor = conn.cursor(as_dict=True)

cursor.execute("select FirstName,LastName,Title from Employees")


#rows=cursor.fetchall()
for row in cursor:
    #print(row)
    print("FirstName=%s"%(row['FirstName']))


#connect.commit()
cursor.close()
conn.close()