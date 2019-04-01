def myselSort(arr):
    for j in range(len(arr)-1):
        temp = j
        for i in range(j,len(arr)-j):
            if arr[i] < arr[j]:
                temp = i
        arr[temp], arr[i] = arr[i], arr[temp]
        print(arr)
myselSort([6,4,5,2,3,1])