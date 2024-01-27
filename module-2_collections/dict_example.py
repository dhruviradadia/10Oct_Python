stdata={'id':101,'name':'dhruvi','sub':'python'}

"""print(stdata)
print(stdata['name'])
print(stdata.get('sub'))
print(len(stdata))

print(stdata.keys())
print(stdata.values())"""

#-----------------------------------------------------#

print(stdata)
"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""if 'name' in stdata:
    print("yes...")
else:
    print("no...")"""

"""if 'dhruvi'in stdata.values():
    print("yes..")
else:
    print("no")"""

#stdata["id"]=102

#stdata["city"]="rajkot"
#stdata.pop('sub')
#del stdata['sub']
stdata.clear()
print(stdata)
