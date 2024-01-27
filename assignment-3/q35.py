l=[{"nm":"dhruvi","city":"rajkot","age":23,"id":131}]

print("original list:",l)

unique_value = set(val for dic in l for val in dic.values())

print("unique values:",unique_value)