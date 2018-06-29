var = input('a b c: \n').split()
a, b, c = int(var[0]), int(var[1]), int(var[2])

d = (((b**2) - (4*a*c))**(1/2))

print((-b + d)/(2*a))
print((-b - d)/(2*a))
