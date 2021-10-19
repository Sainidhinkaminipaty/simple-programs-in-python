# Reverses the elements in a list

a = [3,1,4,1,5,9,2]
n = len(a)
for i in range(n//2):
	(a[i],a[n-i-1]) = (a[n-i-1],a[i])
print a
#example 
'''
input:
[3,1,4,1,5,9,2]
output:
[2,9,5,14,1,3]
'''
