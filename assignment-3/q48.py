pi=22/7
h = float(input('Height of cylinder: '))
r = float(input('Radius of cylinder: '))
volume = pi * r * r * h
sur_area = ((2*pi*r) * h) + ((pi*r**4))
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)
