import math
try:
    A, B, C = list(map(float, input().split()))
    D = (B * B) - (4 * A * C)
    x1 = (-B + math.sqrt(D)) / (2 * A)
    x2 = (-B - math.sqrt(D)) / (2 * A)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')

except ValueError:
    print('Impossivel calcular')
except ZeroDivisionError:
    print('Impossivel calcular')