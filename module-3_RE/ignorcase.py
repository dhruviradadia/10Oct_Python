import re

mystr="This is python!545646"

x=re.findall('[A-Z]',mystr)
#x=re.findall('[a-z]',mystr)
#x=re.findall('[0-9]',mystr)
#x=re.findall('[A-Za-z]',mystr)
#x=re.findall('A-Za-zO-9',mystr)
#x=re.findall('[A-P]',mystr)

print(x)