import functools as f

"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""
def is_k_sum_in_arr(arr, k):
	nums = set()
	for n in arr:
		subk = k - n
		if subk in nums:
			return True
		else:
			nums.add(n)

	return False	


arr = [10, 15, 3, 7]

print(is_k_sum_in_arr(arr, 17))
print(is_k_sum_in_arr(arr, 18))
print(is_k_sum_in_arr(arr, 13))
print(is_k_sum_in_arr(arr, 21))


"""
Given an array of integers, 
return a new array such that each element at index i of the new array is the product of all the numbers in the original array
except the one at i.
For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?

arr  [2, 3, 4, 5]
pre   1  2  6  24
suf   60 20 5  1
res.  60 40 30 24
"""
def product_arr_except(arr):
	pre = [1]; suf = [1]
	auxp = 1; auxs = 1

	leng = len(arr)
	for i in range(0, leng):
		if i < leng-1:
			auxp *= arr[i]
			pre.append(auxp)
		if (leng-1-i) > 0:
			auxs *= arr[leng-1-i]
			suf.append(auxs)

	len_pre = len(pre)
	for i in range(0, len_pre):
		arr[i] = pre[i] * suf[len_pre-i-1]	
	return arr		

def product_arr_except1(arr):
	p = f.reduce(lambda x,y: x*y, arr)
	for i,n in enumerate(arr):
		arr[i] = p / n
	return arr

def product_arr_except2(arr):
	p = f.reduce(lambda x,y: x*y, arr)
	return [p/x for x in arr]

def product_arr_except3(arr):
	p = f.reduce(lambda x,y: x*y, arr)
	return list(map(lambda x: p/x, arr))

arr = [2, 3, 4, 5]
print(product_arr_except(arr))
arr = [2, 3, 4, 5]
print(product_arr_except1(arr))
arr = [1, 2, 3, 4, 5]
print(product_arr_except(arr))
arr = [1, 2, 3, 4, 5]
print(product_arr_except1(arr))
arr = [1, 2, 3, 4, 5]
print(product_arr_except2(arr))
arr = [1, 2, 3, 4, 5]
print(product_arr_except3(arr))


"""
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""
def first_missing_pos_integer(arr):
	tsum = 0
	psum = 0
	for i,n in enumerate(arr):
		if n>0:
			psum+=n
		tsum = tsum+i+1

	res = tsum-psum
	if res == 0:
		return len(arr)
	return res

print(first_missing_pos_integer([3,4,-1,1,-2]))
print(first_missing_pos_integer([3,4,-1,1]))
print(first_missing_pos_integer([1,2,0]))


