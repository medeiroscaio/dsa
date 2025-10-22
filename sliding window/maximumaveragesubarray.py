def findMaxAverage(nums, k):
    n = len(nums)
    curr_sum = 0

    for i in range(0, k):
        curr_sum += nums[i]
    max_avg = curr_sum / k
    for i in range(k, n):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]
        avg = curr_sum / k
        max_avg = max(max_avg, avg)
    return round(max_avg, 5)


result = findMaxAverage([1,12,-5,-6,50,3], 4)
print(result)
