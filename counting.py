import time
start = time.time()

g = open('counting_sorted.txt','w')

h = open('counting_sorted1.txt','w')

t = open('counting_sorted2.txt','w')


def counts(vector):
    l = len(vector)
    maxi = max(vector)
    rez = [0] * l
    nr = [0] * (maxi+1)
    for i in range(0, l):
        nr[vector[i]] += 1

    for i in range(1, maxi+1):
        nr[i] += nr[i-1]
    i = l-1
    while i >= 0:
        rez[nr[vector[i]]-1] = vector[i]
        nr[vector[i]] -= 1
        i -= 1
    for i in range(0, l):
        vector[i] = rez[i]

f = open('date.txt','r')

arr = [int(x) for x in f.read().strip().split()]
counts(arr)

print(arr, file = h)

g.close()
h.close()
t.close()

end = time.time()

print(end-start)

#pt date = 0.10483193397521973
#pt date1 = 0.3603489398956299
#pt date2 = 199.26950573921204
