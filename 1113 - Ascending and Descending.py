flag = True
while flag:
    X, Y = map(int, input().split(' '))

    if X > Y:
        print('Decrescente')
    elif X < Y:
        print('Crescente')
    else:
        flag = False
