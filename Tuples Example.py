tup1 = ("a", "b", "c", "d", "e") # can be of same data type
tup2 = (1.123, True, [1, 2, 3], {"abc": "xyz", "123": "456"}) # can be a mix of different data types
tup3 = (1, 2, 3 , 4, 5, 5, 5) # can have same element multiple times

tup4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tup4[2])
print(tup4[:8])
print(tup4[2:7])
print(tup4[3:])

 
# Tuples are immutable data type, which means their value can not be change using assignment operator.
# They take less space in memory.

print(tup1.__sizeof__())


# Iterating through a tuple.

for item in tup1:
    print(item)

count = 0
while count < len(tup1):
    print(tup1[count])
    count += 1
