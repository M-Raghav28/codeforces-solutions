n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)

total = sum(coins)
current = 0
count = 0

for coin in coins:
    current += coin
    count += 1
    
    if current > total - current:
        break

print(count)