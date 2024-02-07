with open(r"myfile.txt","r")as f:
    l=len(f.readlines())
    print("total number of lines is:",l)