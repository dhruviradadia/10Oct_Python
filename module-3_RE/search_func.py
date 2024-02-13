import re
mystr="this is python!"

x=re.search('this',mystr)
#x=re.search('is',mystr)
print(x)

if x:
    print("match done...")
else:
    print("Error!please input proper string.")    