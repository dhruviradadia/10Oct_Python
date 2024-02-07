try:
    u=int(input("Enter odd number:"))
    if u%2==0:
        raise ValueError ("Even number are not allowed")
    else:
        print("number is:",u)
except ValueError as e:
    print(f"error:{e}")       