"""
Shifted Array Search
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. 
For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.
Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. 
If num isn’t in shiftArr, return -1. Assume that the offset doesn’t equal to 0 (i.e. assume the array is shifted at least once) or to arr.length - 1 (i.e. assume the shifted array isn’t fully reversed).

Example:
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since it’s the index of 2 in arr
"""
def shifted_arr_search(shiftArr, num):
    pivot = findPivot(shiftArr)
    print(pivot)
    
    if pivot == 0 or num < shiftArr[0]:
        return binarySearch(pivot, len(shiftArr), shiftArr, num)
      
    return binarySearch(0, pivot, shiftArr, num)  
  
def findPivot(shiftArr):
    l = 0
    r = len(shiftArr)  
    m = int((l + r) / 2)
    while m>=0 and m<len(shiftArr)-1:
        m = int((l + r) / 2)
        
        if m>=len(shiftArr)-1 or m<0:
          return 0
        
        if shiftArr[m] > shiftArr[m+1]:
            return m
        elif shiftArr[m-1] > shiftArr[m]:
            return m
        elif shiftArr[m-1] < shiftArr[m]:
            l = m
        else:
            r = m
            
    return 0
  
def binarySearch(start, end, shiftArr, num):
    l = start
    r = end    
    m = int((l + r) / 2)
    while m>=0 and m<end:
        m = int((l + r) / 2)
        if shiftArr[m] == num:
            return m
        elif shiftArr[m] > num:
            r = m
        else:
            l = m

    return -1

def findPivotPoint(arr):
    begin = 0
    end = len(arr) - 1

    while (begin <= end):
        mid = begin + int((end - begin)/2)
        if (mid == 0 or arr[mid] < arr[mid-1]):
            return mid
        if (arr[mid] > arr[0]):
            begin = mid + 1
        else:
            end = mid - 1
    return 0
#---------

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
	print(shifted_arr_search([2, 4, 5, 9, 17, 12], 2))
	print(shifted_arr_search([9, 12, 17, 2, 4, 5], 2))  
	print(shifted_arr_search([1,2], 2))
	print(shifted_arr_search([0,1,2,3,4,5], 1))

