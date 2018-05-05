import random
import sys
totals = [0.0]*3
trials = int(sys.argv[1])
for t in range(trials):
	sixes = 0
	for t in range(6):
		if random.randint(1,6) == 6:
			sixes += 1
	if sixes >= 1:
		totals[0] += 1
	sixes = 0
	for t in range(12):
		if random.randint(1,6) == 6:
			sixes += 1
	if sixes >=2:
		totals[1] += 1
	sixes = 0
	for t in range(18):
		if random.randint(1,6) == 6:
			sixes += 1
	if sixes >= 3:
		totals[2] += 1
prob = [x/trials for x in totals] 
print prob
print totals
