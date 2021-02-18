"""
worst case >>> O(n2)
best case  >>> O(n2)  [because for each iteration it will reach n elements]
"""
def selection_sort(data):
    for t in range(len(data)+1):
        big=0
        for i in range(1,len(data)-t):
            if data[big]<data[i]:
                big=i
        data[big],data[i]=data[i],data[big]
        i=1
    return data

input_data=input("enter values(eg:-5 7 63 2):")
input_data=input_data.split()
for k in range(len(input_data)):
    input_data[k]=int(input_data[k])
selection_sort(input_data)
