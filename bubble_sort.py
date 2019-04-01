def mybubbleSort(arr):
    stop = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            stop = 0
        else:
            stop += 1
    if stop == 5:
        return arr
    else:
        return mybubbleSort(arr)
a = mybubbleSort([6,4,5,2,3,1])
print(a)


def bubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
a = bubbleSort([6,4,5,2,3,1])
print(a)

