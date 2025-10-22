vetor = [1, 2, 3 ,4 , 5, 6, 7, 8, 9, 10] 
left = 0
right = len(vetor) - 1
soma = 0
x = 10
while left < right:
  soma = vetor[left] + vetor[right]
  if soma == x:
    print(f'[{vetor[left]}][{vetor[right]}]')
    break
  elif soma > x:
    right -=1
  elif soma < x:
    left +=1 


