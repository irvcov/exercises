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
print("------------------------------1")

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
print("------------------------------2")

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
print("------------------------------3")


"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""
def sentence_in_list(str_words, list_word):
    word = []
    list_wd = []
    for c in str_words:
        word.append(c)
        wd = ''.join(word)
        if wd in list_word:
            list_wd.append(wd)
            word = []
    return list_wd

print(sentence_in_list("thequickbrownfox", ['quick', 'brown', 'the', 'fox']))
print(sentence_in_list("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))
print("------------------------------4")

"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. 
You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
"""
def max_val_subarr(arr, k):
    res = []
    for i in range(0,len(arr)-k+1):
        bigger = 0
        for j in range(i, i+k):
            #print("{0}, {0}".format(j,i))
            bigger = max(bigger, arr[j])
        res.append(bigger)
    return res

print(max_val_subarr([10, 5, 2, 7, 8, 7],3))
print("------------------------------5")


"""
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
"""
def encodingStringFreq(string):
    stk = []
    res = []
    for c in string:
        if len(stk) > 0:
            tmp = stk.pop()
            stk.append(tmp)
            if c != tmp:
                crep = 0
                while len(stk) != 0:
                    stk.pop()
                    crep += 1
                res.append(str(crep))
                res.append(tmp)
                stk.append(c)
            else:
                stk.append(c)
        else:
            stk.append(c)
    if len(stk) > 0:
        tmp = stk.pop()
        stk.append(tmp)
        crep = 0
        while len(stk) != 0:
            stk.pop()
            crep += 1
        res.append(str(crep))
        res.append(tmp)
    return ''.join(res)

def encodingStringFreq2(string):
    res = []
    dic = {}
    before = string[0]
    for c in string:
        if c == before:
            dic[c] = dic.get(c, 0) + 1
        else:
            res.append(str(dic[before]))
            res.append(before)
            del dic[before]
            dic[c] = dic.get(c, 0) + 1
        before = c
    if len(dic) != 0:
        res.append(str(dic[before]))
        res.append(before)
    return ''.join(res)

print(encodingStringFreq("AAAABBBCCDAA"))
print(encodingStringFreq2("AAAABBBCCDAA"))
print(encodingStringFreq("ABBBCCDAA"))
print(encodingStringFreq2("ABBBCCDAA"))
print(encodingStringFreq("ABCDA"))
print(encodingStringFreq2("ABCDA"))
print("------------------------------6")

"""
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. 
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), 
so we can trap 8 units of water.
"""
def water_remain_trapped(arr):
    units = 0
    p1 = 0
    p2 = 1
    l = len(arr)

    while p1 < l and p2 < l:
        wall1 = arr[p1]
        wall2 = arr[p2]

        if wall2 < wall1:
            units += wall1 - wall2
        else:
            p1 = p2

        p2 += 1

    if wall2 < wall1:
        adj_p = p2 - p1 -1
        units += (adj_p * (wall2-wall1))
    
    return units

print(water_remain_trapped([3, 0, 1, 3, 0, 5])) # 8
print(water_remain_trapped([3, 0, 1, 3, 0, 2])) # 5+2+2 = 7
print(water_remain_trapped([1, 3, 1, 5, 0, 5])) # 2+5 = 7
print(water_remain_trapped([3, 0, 1, 5, 0, 1])) # 5+1 = 6
print(water_remain_trapped([3, 0, 1, 5, 0, 1, 0, 2])) # 5+5 = 10
print("------------------------------7")
    
"""
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. 
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""
def subsset_s_adds_up_k(s,k): #Aproach not working
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            subset = s[i:j]
            val = f.reduce(lambda x,y : x+y, subset)
            #print(subset)
            if val == k:
                return subset
    return None

def subsset_s_adds_up_kV2(s,k):
    set1 = set(s)
    s_sorted = sorted(s)
    print(s_sorted)


def subsset_s_adds_up_kV3(s,k):
    s = sorted(s)
    index_end=0
    for i in s:
        if i > k:
            break
        index_end += 1
    s = s[0:index_end]    

    cm = Combination()
    for i in range(1, len(s)):
        for subset in cm.make_combination(s, i):
            #print(subset)
            if f.reduce(lambda x,y : x+y, subset) == k:
                return subset
    return None

# def combinationUtil(arr, data, start, end, index, subset_len, list_subsets):
#   if index == subset_len:
#       list_subsets.append(data)
#       return

#   i=start
#   for i in range((start+i), (i<=end and (end-i+1) >= (subset_len-index)), 1):
#       data[index] = arr[i]
#       combinationUtil(arr, data, i+1, end, index+1, subset_len, list_subsets)

# def make_combination(arr, subset_len):
#   n = len(arr)
#   data = [0 for i in range(subset_len)]
#   list_subsets = []
#   print(data)
#   combinationUtil(arr, data, 0, n-1, 0, subset_len, list_subsets)
class Combination():

    def __init__(self):
        self.list_subsets = []

    def combinationUtil(self, arr, data, index, i, r):
        if index == r:
            #print (data)
            self.list_subsets.append(set(data))
            return 

        if i>=len(arr):
            return

        data[index] = arr[i]
        self.combinationUtil(arr, data, index+1, i+1, r)
        self.combinationUtil(arr, data, index, i+1, r)

    def make_combination(self,arr, subset_len):
        data = [0 for i in range(subset_len)]
        arr = sorted(arr)
        self.combinationUtil(arr, data, 0, 0, subset_len)
        return self.list_subsets

cm = Combination()
print(cm.make_combination([1, 2, 3, 4, 5], 3))
#print(subsset_s_adds_up_kV2([12, 1, 61, 5, 9, 2], 24))
print(subsset_s_adds_up_kV3([12, 1, 61, 5, 9, 2], 24))
print("------------------------------8")

"""
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. 
If no such itinerary exists, return null. 
If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', 
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. 
However, the first one is lexicographically smaller.
"""
def itinerary(flights, start):
    dict_flights = dict()
    for f in flights:
        tmp = dict_flights.get(f[0], [])
        tmp.append(f[1])
        dict_flights[f[0]] = tmp

    result = [start]
    key = start
    idx = 0
    while key in dict_flights and idx <= len(flights):
        tmp = dict_flights[key]
        tmp = sorted(tmp, reverse=True)
        
        if len(tmp) != 0:
            key_ = tmp.pop()
            result.append(key_)
            dict_flights[key] = tmp
            key = key_
        else:
            del dict_flights[key]

        idx += 1

    return result
    
        
print(itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
print(itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))
print("------------------------------9")

"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, 
find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
def non_duplicated(arr):
    suma = f.reduce(lambda x,y : x+y, arr)
    print(float(suma))
    print(float(suma/3.0))

print(non_duplicated([6, 1, 3, 3, 3, 6, 6]))
print(non_duplicated([13, 19, 13, 13]))
print("------------------------------10")

"""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

print("------------------------------11")

"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, 
the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
def segregate_values_rgb(arr):
    p1 = 0
    l_arr = len(arr)
    n_swap = 0
    while p1 < l_arr-1:
        if arr[p1] < arr[p1+1]:
            tmp = arr[p1+1]
            arr[p1+1] = arr[p1]
            arr[p1] = tmp
            n_swap += 1
        p1 += 1

    if n_swap == 0:
        return arr

    return segregate_values_rgb(arr)

print(segregate_values_rgb(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
print("------------------------------12")

"""
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""
def longest_palindromic_substring(str):
    for i in range(len(str), 0, -1):
        j = 0
        while j+i <= len(str):
            substr = str[j:j+i]
            if isPalindrom(substr):
                return substr
            j += 1
    return None

def isPalindrom(wd):
    l_wd = len(wd)
    for i in range(0, l_wd//2 ):
        if wd[i] != wd[l_wd-1-i]:
            return False
    return True

print(longest_palindromic_substring("aabcdcb"))
print(longest_palindromic_substring("bananas"))
print("------------------------------13")

"""
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
def max_profit_arr(arr):
    p1 = 0
    p2 = 1
    max_profit = 0
    while p1 < len(arr) and p2 < len(arr):
        tmp_profit = 0
        if arr[p1] <= arr[p2]:
            tmp_profit = arr[p2] - arr[p1]
        else:
            p1 = p2

        if tmp_profit > max_profit:
            max_profit = tmp_profit

        p2 += 1

    return max_profit


print(max_profit_arr([12, 11, 18, 5, 7, 10])) # 7
print(max_profit_arr([9, 11, 8, 5, 7, 10])) # 5
print(max_profit_arr([9, 11, 8, 5, 7, 10, 1, 7, 6, 10, 4])) # 9
print("------------------------------14")





