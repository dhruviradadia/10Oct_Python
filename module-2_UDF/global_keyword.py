a=34

print("A",a)
def getvalue():
    global a
    a=67
    print("A=",a)


getvalue()    