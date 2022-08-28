"""
 Author: Furqan Fiaz
 Date: 09-08-2022, 4.19 Pm
 This file will contain the information about For Loops in Python
"""
# Define a List

List1=["Captain", "Driver", "Rider", "Umpire","Wrestler","Mechanic","Teacher"]
"""" 
We can print each item in list by wrtiting 7 print statements such as print(List1[0],List1[1],List1[2])
This would do the work but if we have 100000 items in list how can we do it?
This would be done using For loops
"""
for item in List1:
    print(item)

# We can also define a list of list and print it using for loop

List2=[["Captain", 2], ["Driver",30], ["Rider",23], ["Umpire",34],["Wrestler",15],["Mechanic",8],["Teacher",9]]
print("The list of list items and Numbers:")
for items,numbers in List2:
    print(items,numbers)

"""
Same is the case with dictionary
"""
dict1=dict(List2)
print("The values in Dictionary are:",dict1)
for items, numbers in dict1.items():
    print(items,numbers)