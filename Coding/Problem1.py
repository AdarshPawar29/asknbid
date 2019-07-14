d = {}
def candyman(a, n):
    if(n in d):
        return d[n]
    flag = False
    for i in a:
        if(n%i == 0):
            flag = True
            break
    if(flag == False):
        d[n] = 0
        return 0
    for i in a:
        if(n%i == 0 and i%2 == 0):
            d[n] = 1
            return 1
    for i in a:
        if(n%i == 0):
            if(candyman(a, n//i) == 0):
                d[n] = 1
                return 1
    d[n] = 0
    return 0

#Auto-test because I'm lazy to debug manually
debug = True
if debug:
    #test case 1 - expected Almond
    n = 10
    m = 3
    a = [5, 1000000000000000000, 2]
    if(candyman(a, n) == 1):
        print("Almond")
    else:
        print("Cashew")
    #test case 2 - expected Almond
    n = 718791247583033625
    m = 6
    a = [3, 5, 17, 19, 23, 37]
    if(candyman(a, n) == 1):
        print("Almond")
    else:
        print("Cashew")
    #test case 3 - expected Cashew
    n = 328360141446962625
    m = 7
    a = [5, 9, 11, 35, 57, 165, 345]
    if(candyman(a, n) == 1):
        print("Almond")
    else:
        print("Cashew")
else:
    n,m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    if(candyman(a, n) == 1):
        print("Almond")
    else:
        print("Cashew")