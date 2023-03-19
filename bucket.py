
import time
start = time.time()

g = open('bucket_sorted.txt','w')

h = open('bucket_sorted1.txt','w')

t = open('bucket_sorted2.txt','w')

def inserts(bucket):
    for i in range (1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

def buckets(vec):
    maxi = max(vec)
    l= len(vec)
    siz = maxi / l
    b=[]
    for i in range(l):
        b.append([])
    for i in range(l):
        j = int (vec[i] / siz)
        if j != l:
            b[j].append(vec[i])
        else:
            b[l-1].append(vec[i])
    for i in range(0,l):
        inserts(b[i])
    vec.clear()
    for i in range(0,l):
        vec = vec + b[i]
    print(vec, file = t)

f = open('date2.txt','r')

arr = [int(x) for x in f.read().strip().split()]

buckets(arr)

g.close()
h.close()
t.close()

end = time.time()
print(end-start)
#pt data = 20.74340319633484
#pt data1 = 201.0899143218994
#pt data2 = 215.75136399269104
