def bubble(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:   
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)            


arr = [10,4,-5,3,2,999]
bubble(arr)
