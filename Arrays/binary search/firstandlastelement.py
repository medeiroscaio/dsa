def firstAndLastElement(nums, target):
    def find_first():
        lo, hi = 0, len(nums) - 1
        first = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                first = mid
                hi = mid - 1  
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return first

    def find_last():
        lo, hi = 0, len(nums) - 1
        last = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                last = mid
                lo = mid + 1  
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return last

    return [find_first(), find_last()]