# 1. Don't use loops at all

numbers = [10,20,43, 30, 50,70,60,80]
result = 0
for num in numbers:
    result += num

print(f"use iterate for-loop : {result}")
result = sum(numbers)
print(f"use sum() method : {result}")

print("-"*40)
print("use enumerate instead len() method")
print("-"*40)

# 2. use enumerate
numbers = [10,20,43, 30, 50,70,60,80]
"""
for idx in range(len(numbers)):
    print(idx,numbers[idx])

"""
for idx, val in enumerate(numbers, start=1): # counting start with no.1
    print(idx,val)



print("-"*40)
print("use zip()")
print("-"*40)

# 3. use zip
a = [1,2,3,4]
b = ["a","b","c"]

"""
for idx in range(len(a)):
    print(a[idx], b[idx])
"""

for val1, val2 in zip(a,b):
    print(val1, val2)

print("using strict mode True will be error")

# if using strict=True there is some error becouse a number is 4 and b is 3
"""
for val1, val2 in zip(a,b, strict=True):
    print(val1, val2)
"""

print("-"*40)
print("Use a generator")
print("-"*40)

# 4. Use a generator

print("without a generator")
events = [("learn",5), ("learn",10), ("relaxed", 20)]
minutes_studied = 0
for event in events:
    if event[0] == "learn":
        minutes_studied += event[1]
print(minutes_studied)

print("with a generator")
study_times = (event[1] for event in events if event[0] == 'learn')
minutes_studied = sum(study_times)
print(minutes_studied)

print("Notes \n")
print("---------- \n")
print("Warning...be careful if use generator twice in the second value is empty becuse object of generator will zero")
minutes_studied2 = sum(study_times)
print(minutes_studied2)


print("-"*40)
print("Use itertools islice")
print("-"*40)

# 5. use itertools
lines = ["line1","line2","line3","line4","line5", "line6", "line7","line8","line9","line10"]

for i, line in enumerate(lines):
    if i >=5:
        break
    print(line)

print()

# use itertools
from itertools import islice

first_five_lines = islice(lines, 1, 5,2)
for line in first_five_lines:
    print(line)




print("-"*40)
print("Use itertools pairwise")
print("-"*40)

# use pairwise
data ='ABCDEFG'
for i in range(len(data)-1):
    print(data[i],data[i+1])

print()

from itertools import pairwise

for pair in pairwise('ABCDEFG'):
    print(pair[0], pair[1])


print("-"*40)
print("Use itertools takewhile")
print("-"*40)

for item in[1,2,4,-1,4,1]:
    if item >=0:
        print(item)
    else:
        break

print()
print()

from itertools import takewhile

items=takewhile(lambda x:x >=0,  [1,2,4,-1,4,1])
for item in items:
    print(item)

print("-"*40)
print("Use itertools numpy")
print("-"*40)

import numpy as np
vec_a=[1,2,3]
vec_b=[4,5,6]

result = 0
for  val1, val2 in zip(vec_a, vec_b):
    result += val1 * val2
print(result)
print("-"*20)
result= np.dot(vec_a, vec_b)
print(result)


N = 100_000_000

def sum_python():
    return sum(range(N))

def sum_numpy():
    return np.sum(np.arange(N))

print(sum_python())
print(sum_numpy())

import timeit
print("sum python: ", timeit.timeit(sum_python, number=1))
print("sum numpy: ", timeit.timeit(sum_numpy, number=1))


