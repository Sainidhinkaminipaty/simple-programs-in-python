'''
1 It's a naive algorithm to find the longest subarray of numbers which are 

  of same value, but the first value of subarray and last value of subarray should be 

  less than the previous value and next value respectively. So a plateau is found and 

  our code is to find longest one of these plateaus found.

  '''


a = [1,2,2,3,4,4,4,1,5,5,5,5,5,5,0,1,1,1,1,1,1,1,1,1,1,1,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
i = 1
pos = []
len1 = []
while i < len(a):
	if a[i-1] <= a[i]:
		leng = 1
		while a[i] == a[i+1]:
			leng += 1
			i += 1
			

		if a[i+1] < a[i]:
			len1.append(leng)
			posi = i + 1 - leng
			pos.append(posi)
			

			
	i += 1
print(max(len1))
print(pos[len1.index(max(len1))])

