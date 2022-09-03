"""
 Author: Furqan Fiaz
 Date: 25-08-2022, 4.57 Pm
 This file will contain the information about Enumerate function ,main & Join function in Python
"""
# Enumerate function make it easy for us to traverse through list
# we define a list
list1=["Apple","Mango","Watermelon","Grapes","Orange"]
# we want to print those items which are written on odd index in list
i=1
for item in list1:
    if i%2==1:
        print(f"items in odd position are {item}")
    i += 1
# We can do all this usign enumerate function which makes it easy for us
print("\n")
if __name__ == '__main__':
    for index, item in enumerate(list1):
        if index % 2 == 1:
            print(f"items in even position are {item}")

# Join Function
for item in list1:
    print(f"{item}"," and ", end=" ")

print("Other fruits")

# we can do the above work using join function
a=" and ".join(list1)
print("These values are being joined using join function")
print(a)