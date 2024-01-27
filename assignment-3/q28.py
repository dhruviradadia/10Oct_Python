import operator
d = {11: 22, 33: 44, 44: 33, 22: 11, 0: 0}
print('Original dictionary : ',d)
sd = sorted(d.items(), key=operator.itemgetter(1))
print('Ascending order : ',sd)
sd = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Descending order : ',sd)



print('Dictionary in descending order by value :sd')  
