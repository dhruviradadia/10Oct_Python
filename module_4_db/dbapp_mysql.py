import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='newdata')
    print("database connected!")
except Exception as e:
    print(e)    
    cur=db.cursor()