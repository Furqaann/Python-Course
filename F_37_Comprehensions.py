"""
 Author: Furqan Fiaz
 Date:10-09-2022, 12.16 Am
 This file will contain the information about Comprehensions in Python
"""
for i in range(103):
    if i%3==0:
        print(i)

# We can do the above done work using list comprehensions
l1=[i for i in range(103) if i % 3==0]
print(l1)

# Dictionary Comprehensions
dict1={i:f"item{i}" for i in range(1,103) }
print(dict1)

# we can print list using for loop in list
list2=[i for i in range(100)]
print(list2)

"""
This is The End Of Object Oriented Programming, we have covered many important topics through this series
"""