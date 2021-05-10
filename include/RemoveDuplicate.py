def removeDup(arr):
    if 1 > len(arr):
        print("Nothing in array to clean")

    seen_arr = []
    for index, value in enumerate(arr):
        if arr[index] not in seen_arr:
            seen_arr.append(value)
    print(f"Original List: {arr}")
    print(f"Cleaned list: {seen_arr}")

