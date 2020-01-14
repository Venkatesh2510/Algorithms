def maxHeapify(arr,n,i):
    largest=i 
    l=2*i+1
    r=2*i+2
    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=i:
        temp=arr[i]
        arr[i]=arr[largest]
        arr[largest]=temp
        maxHeapify(arr,n,largest)
def heapSort(arr,n):
    for i in range(n,-1,-1):
        maxHeapify(arr,n,i)
    for i in range(n-1,0,-1):
        temp=arr[0]
        arr[0]=arr[i]
        arr[i]=temp
        maxHeapify(arr,i,0)    
arr=[9,12,312,23423,1]
heapSort(arr,len(arr))
print(arr) 