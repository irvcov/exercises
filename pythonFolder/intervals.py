

def intervals(inter):
	inter = sorted(inter, key = lambda x: x[1])

	result = []
	for i in xrange(1, len(inter)-1):
		set1 = inter[i]
		set2 = inter[i+1]

		if(set1[1] == set2[1]):
			result.append("")


def flat_intervals(inter):
	"""
	Example.
	input: [[10, 50], [40, 160], [170, 210], [30, 80]]
		 - sort input
			[[10, 50], [30, 80], [40, 160], [170, 210]]
			       ^     ^   if is bigger join
			[[10, 80], [40, 160], [170, 210]]
                   ^.    ^.  if is bigger join
            [[10, 160], [170, 210]]         
                   ^.    ^.  if is bigger join
	output: [[10, 160],[170,210]]
	"""
	inter = sorted(inter, key=lambda x: x[0])

	result = []
	pr = 0
	result.append(inter[0])
	for i in range(1, len(inter)):
		if result[pr][1] > inter[i][0]:
			if result[pr][1] < inter[i][1]:
				result[pr][1] = inter[i][1]
		else:
			result.append(inter[i])
			pr+=1

	return result


def timePlaner(slotsA, slotsB, dur):
	"""
	Example.
	input:  slotsA = [[10, 50], [60, 120], [140, 210]]
	        slotsB = [[0, 15], [60, 70]]
	        dur = 8
	output: [60, 68]
	"""
	pa = 0
	pb = 0
	start = 0
	end = 0

	while(pa < len(slotsA) and pb < len(slotsB)):
		slota = slotsA[pa]
		slotb = slotsB[pb]

		if slota[0] > slotb[0]:
			start = slota[0]
		else:
			start = slotb[0]

		end = start+dur
		if end <= slotb[1] and end <= slota[1]:
			return [start, end] 

		if slota[1] < slotb[1]:
			pa+=1
		else:
			pb+=1

	return []

inter1 = [[10, 50], [40, 160], [170, 210], [30, 80]]	
inter2 = [[10, 50], [40, 160], [140, 210], [30, 80]]
inter3 = [[10, 50], [60, 160], [140, 210], [70, 80]]

slotsa = [[10, 50], [60, 120], [140, 210]]
slotsb = [[0, 15], [60, 70]]

def main():
	print(" Intervals Excercises! - timePlaner")
	print(timePlaner(slotsa, slotsb, 8))
	print("\n Intervals Excercises! - flat_intervals")
	print(flat_intervals(inter1))
	print(flat_intervals(inter2))
	print(flat_intervals(inter3))
