def binary_search(nums, n, lo, high):
    while lo <= high:
        mid = (lo + high) // 2
        if nums[mid] < n:
            lo = mid + 1
        elif nums[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1

    while i < n and arr[i] < target:
        i *= 2
    
    if i < n and arr[i] == target:
        return i
    
    return binary_search(arr, target, i // 2, min(i, n - 1))

arr = [2,4,6,8,10]
target = 20

result = exponential_search(arr, target)
print(f"Elemento {target} encontrado no índice: {result}")
