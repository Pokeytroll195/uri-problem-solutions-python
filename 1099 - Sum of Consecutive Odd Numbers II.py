N = int(input())
total = 0

for i in range(N):
    X, Y = map(int, input().split())
    if X > Y:
        for j in range(Y+1, X):
            if j % 2 != 0:
                total += j
        print(total)
        total = 0
    if Y > X:
        for j in range(X+1, Y):
            if j % 2 != 0:
                total += j
        print(total)
        total = 0
    if Y == X:
        print(0)
