fibonacci = [0, 1]
for i in range(2, 10):
    nextnum = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(nextnum)
print("Los primeros 10 números de la secuencia de Fibonacci son:")
for num in fibonacci:
    print(num)