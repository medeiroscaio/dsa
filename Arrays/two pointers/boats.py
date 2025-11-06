def boats(peoples, limit):
  peoples.sort()
  i = 0
  j = len(peoples) - 1
  boats= 0

  while i <= j:
    if peoples[i] + peoples[j] <= limit:
      i += 1
    
    j-= 1
    boats += 1
  return boats


result = boats([3,5,3,4], 5)
print(result)
