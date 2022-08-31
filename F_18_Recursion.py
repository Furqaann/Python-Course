"""
 Author: Furqan Fiaz
 Date: 18-08-2022, 10.10 Pm
 This file will contain the information about Recursive vs Iterative Approach in a file in Python
"""
# Factorial using iterative approach

def fac_iterative(n):
    pass
    fac=1
    for i in range(n):
        fac=fac * (i+1)
    return fac


print(fac_iterative(5))
print(fac_iterative(3))

# Factorial using Recursive approach
def fac_recursive(n):
    factorial=1
    if(n==1):
        return 1
    else:
        return n * fac_recursive(n-1)

print(fac_recursive(4))