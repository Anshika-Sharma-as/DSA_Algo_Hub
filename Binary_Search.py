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
        print("Item found at index",middle)
    else:
        print("Oops! Item Not Found")
        
 """
 Example:-
           db = [10,20,30,40,50,60,70,80,90,100]
           
           binary_search(db,10) //Called function
                
           Output:-   Start: 0 End: 3 Middle: 1
                      Start: 0 End: 0 Middle: 0
                      Item found at index 0
 """
