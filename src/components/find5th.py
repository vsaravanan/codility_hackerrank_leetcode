def find_5th_big_num_recursive(arr, k=5):
    if k == 0:
        return float('-inf')

    max_num = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i

    print(arr)
    print(max_index, arr.pop(max_index) )
    return find_5th_big_num_recursive(arr, k - 1) if k > 1 else max_num

arr = [33, 55, 13, 46, 87, 42, 10, 34, 43, 56]
fifth_big_num = find_5th_big_num_recursive(arr)
print("5th largest number is:", fifth_big_num)
