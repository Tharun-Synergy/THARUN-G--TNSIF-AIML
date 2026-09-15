arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [4, 2, 1, 2, 3, 1]

if len(arr1) != len(arr2):
    print("Arrays are Not Equal")
else:
    freq = {}

    for num in arr1:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in arr2:
        if num in freq:
            freq[num] -= 1
        else:
            print("Arrays are Not Equal")
            break
    else:
        equal = True

        for num in freq:
            if freq[num] != 0:
                equal = False
                break

        if equal:
            print("Arrays are Equal")
        else:
            print("Arrays are Not Equal")
