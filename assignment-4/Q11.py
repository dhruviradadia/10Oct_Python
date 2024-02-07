with open("myfile.txt","r") as a,open("abcd.txt","a")as b:
    for i in a:
        b.write(i)
print("task done")        
