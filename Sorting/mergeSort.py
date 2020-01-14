def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    left=[0]*n1
    right=[0]*n2
    i=0
    j=0
    while(i<n1):
        left[i]=arr[l+i]
        i=i+1
    while(j<n2):
        right[j]=arr[m+1+j]
        j=j+1
    i=0
    j=0
    k=l  
    while i<n1 and j<n2:
        if left[i]<=right[j]:
            arr[k]=left[i]
            i=i+1
            k=k+1        
        else:
            arr[k]=right[j]
            j=j+1
            k=k+1
    while i<n1:
        arr[k]=left[i]
        i=i+1
        k=k+1 
    while j<n2:
        arr[k]=right[j]
        j=j+1
        k=k+1
def mergeSort(arr,l,r):
    if l<r: 
        m=(l+(r-1))/2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)
arr=[1000,2,323,324,99]
mergeSort(arr,0,len(arr)-1)
print(arr)