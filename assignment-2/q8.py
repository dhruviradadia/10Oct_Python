def test_number5(x , y):
    
    
    if x == y or abs(x - y) == 5 or (x + y )== 5 :
        return True
    else:
        return False
    

print(test_number5(7 , 2))
print(test_number5(67 ,89))
print(test_number5(3 , 2))
print(test_number5(6 , 1))