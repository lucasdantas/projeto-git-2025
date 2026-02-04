n_inicial: int = int(input())
n_final: int = int(input())

for n in range(n_inicial, n_final + 1):
    if n % 2 == 0:
        print(n)
