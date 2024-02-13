import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='newdata')
    print("database connected!")
except Exception as e:
    print(e)    
    
cur=db.cursor()

#create table
create_tbl="create table studinfo(id integer primary key auto_increment,name text,city text)"
try:
    cur.execute(create_tbl)
    print("Table created!")
except Exception as e: 
    print(e)

 #insert data
insert_data="insert into studinfo(name,city)values('dhruvi','rajkot'),('bhavin','banglor'),('janvi','ahmedabad')" 
try:
    cur.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)

 #update data   
updata_data="delete from studinfo where id=5"
try:
    cur.execute(updata_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)

#delete data
delete_data="delete from studinfo where id=6"
try:
    cur.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)    


#show data 
show_data="select*from studinfo"
try:
    cur.execute(show_data)
    data=cur.fetchall()
    data=cur.fetchmany(3)
    data=cur.fetchone()
    print(data)

    for i in data:
        print(i)

except Exception as e:
    print(e)        
            
            





