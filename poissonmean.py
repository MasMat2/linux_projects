from math import factorial as f
n = 0
k = 0
p = 0.4

for n in range(1,11):
    thor = []
    for k in range(1,n+1):
        coef = ((f(n))/(f(k)*(f(n-k))))
        prob = ((((p)**k)))*((p-1)**(n-k))
        print("N=%s,   K=%s,    coef=%s,     prob=%s"   % (n,k,coef,prob))
    for i in thor:
        toll = 0
        if i*1000000>= 1:
            i = int(i*1000000)
            toll += i
        print(toll)
