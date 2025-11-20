arr = [12, 87, 23, 56, 45, 87, 15]

i = 0
j = len(arr) - 1

while i < j:
    arr[i], arr[j] = arr[j], arr[i]  # swap
    i += 1
    j -= 1

for ele in arr:
    print(ele, end=" ")
