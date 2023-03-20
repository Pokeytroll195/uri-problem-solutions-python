flag = True
while flag:
    M, N = map(int, input().split(' '))

    if M <= 0 or N <= 0:
        flag = False

    else:
        sum = 0

        if M > N:
            for i in range(N, M + 1):
                sum += i
                print(i, end=' ')
            print(f"Sum={sum}")
        elif N > M:
            for i in range(M, N + 1):
                sum += i
                print(i, end=' ')
            print(f"Sum={sum}")
