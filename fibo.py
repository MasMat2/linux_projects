import time

def fib(n):
    if n in memo: return memo[n]
    if n <= 2: f = 1
    else: f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f


num = 100
print('b')
memo = {}
start = time.time()
print(fib(num))
end = time.time()
print(end - start)
print('\n')

start = time.time()
n = num
a = 1
b = 0

for i in range(n):
    c = a + b
    a = b
    b = c
print(c)
end = time.time()
print(end - start)

print(memo)
