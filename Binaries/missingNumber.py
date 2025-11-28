def missingNumber(nums):
  x = 0

  for num in nums:
    x ^= num
  for i in range(len(nums) + 1):
    x ^= i
  return x


print(missingNumber([0,3,1]))