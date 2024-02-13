import re

mystr="This is python!5161"
#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\s',mystr)
#x=re.findall('\S',mystr)
#x=re.findall('\wbthis',mystr)
#x=re.findall('\AThis',mystr)
x=re.findall(r'61\Z',mystr)

print(x)

