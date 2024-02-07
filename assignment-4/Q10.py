l=["abcd","efgh","ijkl"]
with open("myfile.txt","a+")as f:
    for i in l:
        f.write("%s\n"%i)
    print("file written successfully")
f.close()        