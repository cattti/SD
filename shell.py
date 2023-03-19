
g = open('shell_sorted.txt','w')

h = open('shell_sorted1.txt','w')

t = open('shell_sorted2.txt','w')

import time
start = time.time()

def shellsort(vec, l):
    gap = l // 2

    while gap > 0:
        for i in range(gap, l):
            val = vec[i]
            j = i
            while j >= gap and vec[j - gap] > val:
                vec[j] = vec[j - gap]
                j = j - gap
            vec[j] = val
        gap = gap // 2

f = open('date2.txt','r')

arr = [int(x) for x in f.read().strip().split()]
l = len(arr)
shellsort(arr,l)

print(arr, file = g)

g.close()
h.close()
t.close()

end = time.time()
print(end-start)

#pt date = 0.5493998527526855
#pt date1 = 1.5584499835968018
#pt date2 = 1.4101767539978027