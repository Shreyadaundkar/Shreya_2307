def selection(arr):
    for i in range(len(arr)):
        min_idx =i
        for j in range (i + 1 , len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr
print("Selection sort:")
arr=[23,43,11,78,98,45,32,12,67]
print("sorted:",selection(arr))