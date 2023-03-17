maxi = 0
count = 0

for i in range(1, 101):
    x = int(input())
    if maxi == 0 or x > maxi:
        maxi = x
        count = i
print(maxi)
print(count)
