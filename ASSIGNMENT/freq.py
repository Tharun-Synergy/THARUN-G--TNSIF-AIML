arr = [2, 5, 2, 8, 5, 2, 3, 5, 2]

most_frequent = arr[0]
max_frequency = 0

for num in arr:
    frequency = 0

    for x in arr:
        if num == x:
            frequency += 1

    if frequency > max_frequency:
        max_frequency = frequency
        most_frequent = num

print("Most Frequent Element:", most_frequent)
print("Frequency:", max_frequency)
