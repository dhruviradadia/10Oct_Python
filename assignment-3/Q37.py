from collections import Counter
 
my_dict = {'A': 672, 'B':123, 'C': 45, 'D':3956, 'E': 1, 'F': 69}
 
k = Counter(my_dict)
 
highest= k.most_common(3) 
 
print("Dictionary with 3 highest values:")
print("Keys: Values")
 
for i in highest:
    print(i[0]," :",i[1]," ")