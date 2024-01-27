list = [2,3,4,5,6,7,8,90,3,33,44]
 

print("The original list : " + str(list))
 
sublist = [8, 2, 1]
res = False
for i in range(len(list) - len(sublist) + 1):
    if list[len(sublist)]:
        res = True
        break
 

print("Is sublist present in list ? : " + str(res))