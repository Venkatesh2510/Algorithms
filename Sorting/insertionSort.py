def insertionSort(arr):
    for i in range(1,len(arr)):
        hold=arr[i]
        j=i-1
        while (arr[j]>hold and j>=0):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=hold   
    print(arr)     
arr=[10,999,-2,10000,19]
insertionSort(arr)        
