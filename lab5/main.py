def mergeSort(Array: list):
    if len(Array) > 1:
        mid = len(Array) // 2
        Left = Array[:mid]
        Right = Array[mid:]
        mergeSort(Left)
        mergeSort(Right)
        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                Array[k] = Left[i]
                i += 1
            else:
                Array[k] = Right[j]
                j += 1
            k += 1


        while i < len(Left):
            Array[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            Array[k] = Right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = input('Enter your array: ').split()
    arr = [int(item) for item in arr]
    print("Unsorted array is", end="\n")
    print(*arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    print(*arr)