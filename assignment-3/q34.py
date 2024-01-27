from collections import Counter

d1={"a":200,"b":100,"c":560}
d2={"a":100,"b":200,"c":100}

d=Counter(d1)+Counter(d2)

print(d)