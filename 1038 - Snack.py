x,y = list(map(int,input().split()))

if x == 1:
    price = 4 * y
elif x == 2:
    price = 4.5 * y
elif x == 3:
    price = 5 * y
elif x == 4:
    price = 2 * y
elif x == 5:
    price = 1.5 * y

print(f"Total: R$ {price:.2f}")
