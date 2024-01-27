l = [("x", 15), ("x", 32), ("x", 63), ("y", 21), ("y", 92), ("z", 31)]


d = {}
for a, b in l:
    
    d.setdefault(a, []).append(b)


print(d)