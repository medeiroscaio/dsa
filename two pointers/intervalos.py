vetor = [1, 2, 3, 4]
circular = vetor + vetor
x = 4
n = len(vetor)

l = 0
r = 0
soma = circular[0]
contador = 0

while l < n and r < 2 * n:
    if soma == x:
        contador += 1
        soma -= circular[l]
        l += 1
    elif soma < x:
        r += 1
        if r < 2 * n:
            soma += circular[r]
    else:  
        soma -= circular[l]
        l += 1

print(contador)