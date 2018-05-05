'''
1 The code is written based on Sieve of Eratosthenes algorithm

2 It is used to count the number of prime numbers less than given input

3 For small inputs a naive algorithm is enough to count the number of primes but as input increses the efficiency of program decreases and so Sieve of Eratosthenes algorithm can be used to increase efficiency of it

'''


import sys
n = int(sys.argv[1])
isPrime = []
for i in range(n+1):
	isPrime += [True]
for i in range(2,n+1):
	if isPrime[i]:
		for j in range(i,n//i+1):
			isPrime[i*j]=False
counts = 0

for i in range(2,n+1):
	if isPrime[i]:
		counts += 1
print counts