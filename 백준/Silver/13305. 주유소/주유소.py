# 주유소

N = int(input())

road = list(map(int, input().split()))
oil = list(map(int, input().split()))

oil_min = oil[0]
price = 0

for i in range(N-1):
    if oil[i] < oil_min:
        oil_min = oil[i]
    price += road[i] * oil_min

print(price)