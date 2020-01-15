def binarySearch(arr,target,l,h):
    while l<=h:
        mid=l+(h-1)/2
        if arr[mid]==target:
            print("Element found at: ",mid)
            return
        elif(arr[mid]<target):
            l=mid+1
        else:
            h=mid-1        
    print("Element not found") 
    return       
arr=[12,9,2,1,123,4255]
arr.sort()
print(arr)
binarySearch(arr,123,0,len(arr))    
