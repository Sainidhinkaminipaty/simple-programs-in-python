# This program prints out random sample(with unique values)

# Each element is equally probable. Prints out random sample(m unique values) from desired population equal to n.

# It is similar to random.sample(population,k) function by Python 3
import sys
import random
m = int(sys.argv[1])
n = int(sys.argv[2])
samp =[]
for i in range(n):
	samp += [i]
for i in range(m):
	r = random.randrange(i,n)
	samp[r],samp[i] = samp[i],samp[r]
print(samp[0:m])