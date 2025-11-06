def fruitsTree(fruits):
  l = 0
  r = 0
  _max = 1
  counter = {}
  counter[fruits[r]] = 1
  while r < len(fruits) - 1:
    r+=1
    if counter.get(fruits[r]):
      counter[fruits[r]] += 1
    else:
      counter[fruits[r]] = 1
    while len(counter) > 2:
      counter[fruits[l]] -= 1
      if counter[fruits[l]] == 0:
          counter.pop(fruits[l])
      l +=1
    _max = max(_max, r - l + 1)
  return _max













result = fruitsTree([0,2,1,2,2,2,2,2,1])
print(result)