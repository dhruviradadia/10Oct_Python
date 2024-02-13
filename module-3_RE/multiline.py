import re

mystr="This is python !124356565"

#x=re.findall('^this',mystr)
x=re.findall('^[A-Z]',mystr)
#x=re.findall('85$',mystr)

print(x)
