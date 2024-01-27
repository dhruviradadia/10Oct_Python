a1=int(input("Enter your physics marks:"))
a2=int(input("Enter your chemastry marks:"))
a3=int(input("Enter your maths marks:")) 


if a1>=40  and a2>=40 and a3>=40:
    total=a1+a2+a3
    print("total:" ,total)

    pr=total/3
    print("pr:" ,pr)

    if pr>=70:
        print("Result:A+")
    elif pr>=60:
        print("Result:A")
    elif pr>50:
        print("Result:B")
    elif pr>40:
        print("Result:C")
else:
    print("Result:FAIL")