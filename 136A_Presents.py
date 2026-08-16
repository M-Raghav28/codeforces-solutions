n = int(input())
a = list(map(int, input().split()))

answer = [0] * n

for i in range(n):
    answer[a[i] - 1] = i + 1

print(*answer)