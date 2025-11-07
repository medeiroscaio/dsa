def BubbleSort(nums):
  n = len(nums)
  for j in range(n - 1):           
      trocou = False              
      for i in range(n - 1 - j):   
          if nums[i] < nums[i + 1]:
              nums[i], nums[i + 1] = nums[i + 1], nums[i]
              trocou = True
      print(nums)
      if not trocou:               
          break
  return nums


BubbleSort([2,1,3,5,8])


def BubbleSortName(names):
  n = len(names)
  for j in range(n - 1):           
      trocou = False              
      for i in range(n - 1 - j):   
          if names[i] > names[i + 1]:
              names[i], names[i + 1] = names[i + 1], names[i]
              trocou = True
      print(names)
      if not trocou:               
          break
  return names


BubbleSortName(["Caio", "Ana", "João", "Luiza", "Matheus"])