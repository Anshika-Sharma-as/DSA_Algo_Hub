""" Time Complexity:
        Best Case - O(log n)
        Worst Case - O(1) """
def binary_search(db,value):
    start = 0
    end = len(db)-1
    middle = int((start+end)/2)
    
    while (db[middle]!=value and start<=end):
        if value > db[middle]:
            start=middle+1
        else:
            end = middle-1
        middle=int((start+end)/2)
        print("Start:",start , "End:",end,"Middle:",middle)
    
    if db[middle]==value:
        print("we found at index",middle)
    else:
        print("Oops! Item Not Found")
