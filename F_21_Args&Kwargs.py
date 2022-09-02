"""
 Author: Furqan Fiaz
 Date: 21-08-2022, 6.31 Pm
 This file will contain the information about *args & **kwargs in a file in Python
"""
#When ever we want to store data and print it we can easily do it using different methods(functions, print)
def print_data(a,b,c,d):
    print(f"The name of personals are {a} {b} {c} {d}")

print_data("Ali","Ahmed","Sajjid","Iqbal")

# However we can use args and kwargs to parse data.
# args and kwargs are optional
def args_print(*args,**kwargs):
    print(*args)
    for item in kwargs:
        print(kwargs)
    # print(type(*args))

# args=["Programmer","Teacher","Officer","Student"]
# Similarly if we want to add new persons data we can easily do it.
args=["Programmer","Teacher","Officer","Student","Security","CEO"]
args_print(*args)

# similarly if we want to print complete dictionary
data={"Ali":"President","Ahmed":"CEO","Sajid":"Teacher"}
args_print(*args,**data)