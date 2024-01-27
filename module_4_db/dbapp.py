import sqlite3

try:
    db=sqlite3.connect("stdata.db")
    print("database conncted !")

except Exception as e:
    print(e)   

tbl_create="create table studinfo(id integer primary key autoincrement,name text,city text)"

try:
    db.execute(tbl_create)
    print("database conncted !")

except Exception as e:
    print(e)   
insert_data="insert into studinfo(name,city)values('dhruvi','kotdapitha')"  
try:
    db.execute(insert_data)
    db.commit()
    print("database conncted !")

except Exception as e:
    print(e)

update_data="update studinfo set name='bhavin',city='banglor' where id=13" 

try:
    db.execute(update_data)
    db.commit()
    print("database conncted !")

except Exception as e:
    print(e)




