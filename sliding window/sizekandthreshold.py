def sizeKAndThreshold(nums, k, t):
    n = len(nums)
    curr_sum = 0
    count = 0

    for i in range(0, k):
        curr_sum += nums[i]
    avg = curr_sum / k
    if avg >= t:
        count += 1
    for i in range(k, n):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]
        avg = curr_sum / k
        if avg >= t:
            count += 1
    return count



result = sizeKAndThreshold([11,13,17,23,29,31,7,5,2,3], 3, 5)
print(result)
