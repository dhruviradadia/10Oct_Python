import re
unm=input("Entre your username:")
unm_pattern="[a-z]+[0-9]+[@]+[.]"

x=re.findall(unm_pattern,unm)


if x: #true

    print("Valied username!")

else:
    print("error!")    

    
