import numpy as np

def linear_search(data,find):
    for i in range(len(data)):
        if data[i]==find:
            print("found at position:",i)
        i+=1
    print("data is not present in the input_data")
input_data=
find=int(input("enter the data to be search:"))
linear_search(input_data,find)
