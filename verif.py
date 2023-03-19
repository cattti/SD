
#date - 100.000 de nr cu valori intre 0 si 70.000
#date1 - 200000 de nr cu valori intre 0 si 1.000.000
#date2 - 200000 de nr cu valori intre 0 si 1.000.000.000

import random

f = open('date2.txt', 'w')

arr = [random.randint(0,1000000000) for _ in range(200000)]

for i in arr:
    f.write(str(i))
    f.write('\n')
