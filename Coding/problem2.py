########################################################## Question 2: The Prime #################################################################

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

def NthFibo(n, ans, mod):
    if(n == 0):
        arr = [0, 1]
        ans[:] = arr
        return
    NthFibo(n//2, ans, mod)
    a = ans[0]
    b = ans[1]
    c = (2 * b) % mod - a
    if(c < 0):
        c += mod
    c = (a % mod * c % mod) % mod
    d = ((a % mod * a % mod) % mod + (b % mod * b % mod) % mod) % mod
    if(n & 1):
        arr = [d, c + d]
        ans[:] = arr
    else:
        arr = [c, d]
        ans[:] = arr

n, m = list(map(int, input().split()))

array = [int(x) for x in input().split()]

s = 0

for i in array:
    if(isPrime(i)):
        ans = [0, 0]
        NthFibo(i + 1, ans, m)
        s += ans[0]
        #print(ans[0], end = ' ')
    
print('Tx({}) = {}'.format(n, s))


# Time Complexity: O(N * Sqrt(N) * Log(N)) where N is the size of array, 
# Space Complexity: Constant Space.
