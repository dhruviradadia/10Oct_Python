n=input("enter line number:")
with open ("myfile.txt","r")as a:
    b=a.readlines()
    print(b[-1]) 
