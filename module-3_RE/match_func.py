import re

mystr="this is python!"

x=re.match('this',mystr)
print(x)

if x:
    print("match done...")
else:
    print("Error!please input proper string.")    