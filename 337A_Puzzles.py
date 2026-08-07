n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

min_diff = float('inf')

for i in range(m - n + 1):
    diff = arr[i + n - 1] - arr[i]
    min_diff = min(min_diff, diff)

print(min_diff)