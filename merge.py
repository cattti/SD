
import time
start = time.time()

g = open('merge_sorted.txt','w')

h = open('merge_sorted1.txt','w')

t = open('merge_sorted2.txt','w')


def mergesort(vec):
    if len(vec) > 1:
        m = len(vec)//2
    
        l = vec[:m]
        r = vec[m:]

        mergesort(l)
        mergesort(r)
        merge(vec,l,r)

def merge(vec,l,r):
        i= 0
        j= 0
        z= 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                vec[z] = l[i]
                i=i+1
            else:
                vec[z] = r[j]
                j=j+1
            z=z+1
        while i < len(l):
            vec[z]=l[i]
            i+=1
            z+=1
        while j < len(r):
            vec[z]=r[j]
            j+=1
            z+=1

f = open('date.txt','r')

arr = [int(x) for x in f.read().strip().split()]
mergesort(arr)

print(arr, file = t)

g.close()
h.close()
t.close()

end = time.time()
print(end - start)
#pt date = 0.31874585151672363
#pt date1 = 0.7230360507965088
#pt date2 = 0.6839258670806885