def closestElements(nums, k, x):
    l, r = 0, len(nums) - k
    while l < r:
        mid = (l + r) // 2
        if x - nums[mid] > nums[mid + k] - x:
            l = mid + 1
        else:
            r = mid
    return nums[l:l + k]

result = closestElements([2, 3, 4, 5, 6, 7], 3, 5)
print(result)
