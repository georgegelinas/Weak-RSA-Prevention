from Crypto.PublicKey import RSA


secparam = 2048

key = RSA.generate(secparam)
public_key = key.publickey()

open('key.pub','w').write(public_key.exportKey())
open('key.priv','w').write(key.exportKey)


def wienerAttack(n,e):
    x = e
    y = n
    # converts rational e/n fraction into a list of partial quotients
    a = x//y
    print(a)
    pq = [a]
    while a * y != x:
        x,y = y,x-a*y
        a = x//y
        pq.append(a)

    # computes the list of convergents using the list of partial quotients
    con = []
    for i in range(len(pq)):
        f = pq[0:i]
        if len(f) == 0:
            con.append((0, 1))
        num = f[-1]
        denom = 1
        for _ in range(-2,-len(f)-1,-1):
            num, denom = f[_]*num+denom, num
        con.append((num, denom))

    for k,d in con:
        if k != 0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1

            # check if the equation x^2 - s*x + n = 0
            # and has integer roots
            discr = s*s -4*n
            if(discr >= 0):
                t = perfectSquare(discr)
                if t != -1 and (s+t)%2 == 0:
                    print("Hacked")
                    return d

def bitLength(x):
    assert x >= 0
    n = 0
    while x > 0:
        n = n+1
        x = x>>1
    return n

def isSqrt(n):
    if n < 0:
        raise ValueError

    if n == 0:
        return 0

    a,b = divmod(bitLength(n),2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def perfectSquare(n):
    h = n & 0xF
    if h > 9:
        return -1
    if (h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8):
        t = isSqrt(n)
        if t*t == n:
            return t
        else:
            return -1
    return -1

