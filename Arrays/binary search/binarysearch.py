def binary_search(nums,n):
  lo = 0
  high = len(nums) - 1
 
  while lo <= high:
    mid = (lo + high) // 2
    if nums[mid] < n:
      lo = mid 
    elif nums[mid] > n:
      high = mid 
    else: 
      print(n)
      return mid


a = [1,2,3,4,5]
binary_search(a, 4)