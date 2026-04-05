import math, time
def find_root(vals=(8, 2)):
    try:
        begin = time.time()
        if type(vals) != tuple:
            vals = (vals, 3)
        a = 0
        if vals[1] < 0:
            posroot = -vals[1]
        else:
            posroot = vals[1]
        d = [100000, 10000, 1000, 100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001, 0.00000000001, 0.000000000001, 0.0000000000001, 0.00000000000001]
        for i in range(len(d)):
            if time.time()-begin > 0.02:
                break
            w = d[i]
            while math.pow(a, posroot) <= vals[0]:
                if time.time()-begin > 0.02:
                    break
                a = a+w
            a = a-w
            continue
        a = round(a, 16)
        if vals[1] < 0:
            a = 1/a
        return(a)
    except OverflowError:
        print('Number or root too large!')
        return None

while True:
    try:
        q = (input('>>'))
        start = time.time()
        print(find_root(eval(q)))
        #print(f'Time taken: {(time.time()-start)} seconds.')
    except ValueError:
        print('Exiting program.')
        break