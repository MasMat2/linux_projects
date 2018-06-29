#
# pi = 3.141592653
# h =1.715
# def unity(lenght):
#     square = lenght**(1/3)
#     circle = ((3*lenght)/(4*pi))**(1/3)
#     cylinder = (lenght/(pi*h))**(1/2)
#     return square, circle, cylinder
#
# sq, cir, cy = unity(1)
# print(h*pi*(cy**2))
# sq_area = sq*6
# cir_area = (cir**2)*4*pi
# cy_area = pi*((cy/h)**2) + 2*pi*cy*h
#
# print(sq_area, cir_area, cy_area)

# a = 'abcdefghijklmnopqrstuvwxyz'
# b = 'cdefghijklmnopqrstuvwxyzab'
# crypt = "map g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# decry = ''
#
# for i in crypt:
#     new = i
#     if i in a:
#         ind = a.index(i)
#         decry += b[ind]
#         continue
#     decry += new
# print(decry)


# def combinations(num):
#     total_sum = 0
#     factors = []
#     for i in range(num):
#         factors.append(i+1)
#     factors.reverse()
#
#     for i in range(num):
#         factorial = 1
#         for a in range(i+1):
#             factorial *= factors[a]
#         print(factorial)
#         total_sum += factorial
#
#     return total_sum
#
#
#
# print(combinations(7))

# primes = [2]
#
# for num in range(2,6805):
#     num += 1
#     a = True
#     for prime in primes:
#         if not a:
#             break
#         if num%prime == 0:
#             a = False
#     if a:
#         primes.append(num)
# primes = primes[::-1]
#
# # for prime in primes:
# #     for i in range(prime-1):
# #         a = prime*(i+1)
# #         n = a**(1/2)
# #         if n == int(n):
# #             print(prime,n,a)
#
# for prime in primes:
#     prime2 = 6805 - prime
#     if prime2 in primes:
#         print(prime2, prime)


# alpha = 'abcdefghijklmnopqrstuvwxyz'
# vigenere = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
# key = 'fu'.lower()
# message = 'authority'.lower()
# encrypt = ''.lower()
# decrypt = ''
#
# place = 0
# for i in message:
#     if place == len(key):
#         place = 0
#     if i not in alpha:
#         encrypt += i
#         continue
#
#     letter = alpha.index(i) + alpha.index(key[place])
#     encrypt_let = vigenere[letter]
#     encrypt += encrypt_let
#     place += 1
#
# print(encrypt)


# #Problem 1
# for a in alpha:
#     key = a + 'o'
#     decrypt = ''
#     place = 0
#     for i in encrypt:
#         if place == len(key):
#             place = 0
#         if i not in alpha:
#             decrypt += i
#             continue
#
#         letter = vigenere.index(i) - vigenere.index(key[place]) + len(alpha)
#         decrypt_let = vigenere[letter]
#         decrypt += decrypt_let
#         place += 1
#
#     print(decrypt)

#
# decrypt = ''
# place = 0
# for i in encrypt:
#     if place == len(key):
#         place = 0
#     if i not in alpha:
#         decrypt += i
#         continue
#
#     letter = vigenere.index(i) - vigenere.index(key[place]) + len(alpha)
#     decrypt_let = vigenere[letter]
#     decrypt += decrypt_let
#     place += 1
#
# print(decrypt)

# p2me = 'planning'.lower()
# p2en = 'uffhscsa'.lower()
#
# keys = []
#
# place = 0
# for i in p2me:
#     print(alpha.index(i),alpha.index(p2en[place]))
#     key = alpha.index(p2en[place]) - alpha.index(i)
#     keys.append(key)
#     place += 1
#
# print(keys)

# num_ind = [9,23,14,14,18,5]
# place = 0
# for i in alpha:
#     key = ''
#     new_ind = [i + place + 17 for i in num_ind]
#     place += 1
#     for ind in new_ind:
#         key += vigenere[ind]
#     print(key)
# print(new_ind)


string = '1c7bb1ae67670f7e6769b515c174414278e16c27e95b43a789099a1c7d55c717b2f0a0442a7d49503ee09552588ed9bb6eda4af738a02fb31576d78ff72b2499b347e49fef1028182f158182a0ba504902996ea161311fe62b86e6ccb02a9307d932f7fa94cde410619927677f94c571ea39c7f4105fae00415dd7d'
string2 = '2710e45014ed7d2550aac9887cc18b6858b978c2409e86f80bad4b59ebcbd90ed18790fc56f53ffabc0e4a021da2e906072404a8b3c5555f64f279a21ebb60655e4d61f4a18be9ad389d8ff05b994bb4c194d8803537ac6cd9f708e0dd12d1857554e41c9cbef98f61c5751b796e5b37d338f5d9b3ec3202b37a32f'
enctr = int(string2, 16)

primes = [2]
#
# for i in range(2,100000):
#     jackpot = True
#     for prime in primes:
#         if not jackpot:
#             break
#         if i%prime == 0:
#             jackpot = False
#     if jackpot:
#         primes.append(i)

# for i in range(len(primes)):
#     other = 1
#     for prime_ind in range(i+1):
#         other *= primes[prime_ind]
#     other += 1
#     if other not in primes:
#         primes.append(other)
#         primes.sort()
#
# other = 1
# for prime_ind in range(len(primes)):
#     other *= primes[prime_ind]
# other += 1
# if other not in primes:
#     # primes.append(other)
#     primes.sort()
# print(primes)


print(primes)

# def isitprime(num):
#     probable_factors = [2,3]
#     maxn = int(num**(1/2))
#     minn = 2
#     if num < 2:
#         return False
#     if num in [2,3]:
#         return True
#
#     for i in range(minn,maxn+1):
#         if i%2 == 0:
#             continue
#         if i%3 == 0:
#             continue
#         probable_factors.append(i)
#
#     prime = True
#     for factor in probable_factors:
#         if not prime:
#             break
#         if (num%factor) == 0:
#             prime = False
#     return prime, len(probable_factors)

def isitprime(num):
    maxn = int(num**(1/2))
    minn = 2

    if num < 2:
        return False
    if num in [2,3]:
        return True
    if num%2 == 0 or num%3 == 0:
        return False


    prime = True
    for factor in range(minn,maxn+1):
        if factor%2 == 0:
            continue
        if factor%3 == 0:
            continue
        if (num%factor) == 0:
            return False
    return prime

def isitprime1(num):
    maxn = int(num**(1/2))
    minn = 2

    if num < 2:
        return False
    if num in [2,3]:
        return True
    if num%2 == 0 or num%3 == 0:
        return False

    prime = True
    for i in range(maxn):
        i += 1
        if (6*i) -1 > maxn:
            break

        for one in [-1,1]:
            factor = 6*i + one
            if factor > maxn or factor < 2:
                break
            if (num%factor) == 0:
                return False, factor

    return prime


print(isitprime1(3999944000147))



# for a in range(10000000):
#     a += 1
#     if isitprime(a) != isitprime1(a):
#         print(a)

# print(isitprime1(100000024351))
# 1000024351, 10000024351
# for prime in primes:
#     if enctr < prime:
#         continue
#     if enctr%prime == 0:
#         print(prime)
