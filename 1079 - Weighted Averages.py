N = int(input())

for i in range(N):
    X, Y, Z = map(float,input().split())
    avg = (X*2 + Y*3 + Z*5)/10
    print("%0.1f"%avg)
