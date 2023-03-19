import time
start = time.time()

g = open('radix_sorted.txt','w')

h = open('radix_sorted1.txt','w')

t = open('radix_sorted2.txt','w')


def count(vector, poz):
    l = len(vector)
    rez = [0] * (l)
    nr = [0] * (10)

    for i in range(0, l):
        index = vector[i]//poz
        nr[index%10] += 1

    for i in range(1, 10):
        nr[i] += nr[i-1]

    i = l-1
    while i >= 0:
        index = vector[i] //poz
        rez[nr[index % 10]-1] = vector[i]
        nr[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(vector)):
        vector[i] = rez[i]


def radix(vector):
    pozz = 1
    maxi = max(vector)
    while maxi > 1:
        count(vector,pozz)
        pozz = pozz * 10
        maxi = maxi/10


f = open('date2.txt','r')

arr = [int(x) for x in f.read().strip().split()]
radix(arr)

print(arr, file = g)

g.close()
h.close()
t.close()

end = time.time()

print(end-start)

#pt date = 0.257000207901001
#pt date1 = 0.989595890045166
#pt date2 = 1.2149379253387451