"""
best case  >>> O(1)
worst case >>> O(n)
"""

def linear_search(data,find):

    for i in range(len(data)):
        if data[i]==find:
            print("found at position:",i)
        i+=1
    print("data is not present in the input_data")

input_data=input("enter values(eg:-5 7 63 2):")
find=int(input("enter the data to be search:"))
input_data=input_data.split()
for k in range(len(input_data)):
    input_data[k]=int(input_data[k])
linear_search(input_data,find)
