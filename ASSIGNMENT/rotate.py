def rotate(arr,k):
    k = k % len(arr)
    arr = arr[-k:] + arr[:-k]
    print("Rotated Array:", arr)
    return
arr = [1, 2, 3, 4, 5]
k = 2
rotate(arr,k)
