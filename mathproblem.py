
for i in range(10000000):
    rad = (i**3)+(i**2)+i+1
    root = ((rad-1)*4)+1
    res = root**(1/2)
    if res.is_integer():
        s = (1+res)/2
        r = (1-res)/2
        s2 = s**2
        r2 = r**2
        if s2 == rad and s.is_integer():
            print(s)
        if r2 == rad and r.is_ineger():
            print(r)
