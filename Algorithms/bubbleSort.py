def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        swapped=False
#inner loop to compair the adjacent element
        for i in range(n):
            if arr[i]>arr[i+1]:
                 arr[i],arr[i+1] =arr[i+1],arr[i]
                 swapped=True
        if not swapped:
            break
arr=[39, 12, 18, 85, 72, 10, 2, 18]  
print("unsorted list in the given list :",arr) 
bubble_sort(arr) 
print("sorted list",arr)
        #######################################
