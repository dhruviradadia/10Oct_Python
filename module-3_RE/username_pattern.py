import re

unm=input("Enter your username:")

unm_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattern,unm)

if x:
    print("valid username!")
else:
    print("Error! invalied username")    