def partition(arr,l,h):
    pivot=arr[h] 
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i=i+1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[i+1]
    arr[i+1]=arr[h]
    arr[h]=temp
    return i+1         
def quickSort(arr,l,h):
    if l<h:
        p=partition(arr,l,h)
        quickSort(arr,l,p-1)
        quickSort(arr,p+1,h)

arr=[9129,2,123,23,90]
quickSort(arr,0,len(arr)-1)
print(arr)
