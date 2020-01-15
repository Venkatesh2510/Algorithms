def linearSearch(arr,target):
    for i in range(0,len(arr)):
        if(target==arr[i]):
            print("Element present at index:",i) 
            return 0
    print("Element not found"); 
    return 0       
arr=[9,2,1,4,5,10,213,3443]
x=linearSearch(arr,213)
