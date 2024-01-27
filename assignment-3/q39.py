from collections import defaultdict, Counter

str1 = 'dhruviradadia'

d = {}

for i in str1:
    
    
    d[i] = d.get(i, 0) + 1

print(d) 