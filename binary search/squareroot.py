def square_root(x):
    if x == 0:
        return 0
    
    lo = 1
    high = x
    
    while lo <= high:
        mid = (lo + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            high = mid - 1
        else:
            lo = mid + 1
    
    return high  

result = square_root(2)
print(result)