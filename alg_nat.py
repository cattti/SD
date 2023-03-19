import time
start = time.time()

f = open('date2.txt','r')

arr = [int(x) for x in f.read().strip().split()]
arr.sort()

end = time.time()

print(end-start)

#pt date = 0.054826974868774414
#pt date1 = 0.10686492919921875
#pt date2 = 0.1113729476928711
