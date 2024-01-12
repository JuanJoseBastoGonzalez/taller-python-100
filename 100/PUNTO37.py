N = 5  
M = [[0 for _ in range(N)] for _ in range(N)]  
for i in range(N):
    for j in range(N):
        M[i][j] = 1

for i in range(3, N + 1):
    espacios = " "
    for _ in range(1, i):
        espacios += " "
    print(espacios, end="")
    for j in range(1, i):
        M[i - 1][j - 1] = M[i - 2][j - 1] * (i - 1) * (j - 1)

        val = M[i - 1][j - 1]
        if val > 0:
            print(val, end=" ")
        else:
            print(" ", end=" ")
    print()
