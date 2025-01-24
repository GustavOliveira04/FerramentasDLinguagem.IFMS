#Uva11679
#Sub-prime

# Resolução:

while True:
    B, N = map(int, input().split())
    if B == 0 and N == 0:
        break 
 
    reservas = list(map(int, input().split()))
    for _ in range(N):
        D, C, V = map(int, input().split())
        reservas[D - 1] -= V
        reservas[C - 1] += V
    saldo_suficiente = all(reserva >= 0 for reserva in reservas)
    if saldo_suficiente:
        print("S")
    else:
        print("N") 