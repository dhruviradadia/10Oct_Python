def data_list(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True

                return result
            
print(data_list([1,3,5,6,8,9],[1,4,5,7,8,9]))
print(data_list([1,2,3,4,6,8],[4,6,7,8,8]))