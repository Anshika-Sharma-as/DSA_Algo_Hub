"""
time complexity:
---------------
worst case >>> O(n2)  [because every is not in their sorted positions]
best case  >>> O(n)   [because the input is sorted already so need to
                       compare n elements n times again just one iteration
                       is enough!]
"""
def bubble_sort(data):
    for t in range(len(data)):
        trigger=0
        for i in range(len(data)-t-1):
            if data[i]>data[i+1]:
                data[i],data[i+1]=data[i+1],data[i]
                trigger=1
        i=0
        if trigger==0:
            break
    return data

input_data=input("enter values(eg:-5 7 63 2):")
input_data=input_data.split()
for k in range(len(input_data)):
    input_data[k]=int(input_data[k])
bubble_sort(input_data)

