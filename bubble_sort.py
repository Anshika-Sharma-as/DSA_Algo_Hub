def bubble_sort(data):
    for t in range(len(data)):
        for i in range(len(data)-t-1):
            if data[i]>data[i+1]:
                data[i],data[i+1]=data[i+1],data[i]
        i=0
    return data

input_data=input("enter values(eg:-5 7 63 2):")
input_data=input_data.split()
for k in range(len(input_data)):
    input_data[k]=int(input_data[k])
bubble_sort(input_data)

