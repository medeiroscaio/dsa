def remove_element(nums, value):
    k = 0
    for i in range(len(nums)):
        if nums[i] != value:
            nums[k] = nums[i]
            k += 1
    return k  



nums = [1,2,3,4,5,6,3,4,5,3]
k = remove_element(nums, 3)
print(k) 