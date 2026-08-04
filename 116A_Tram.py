n = int(input())

current = 0
max_people = 0

for _ in range(n):
    a, b = map(int, input().split())
    
    current -= a
    current += b
    
    max_people = max(max_people, current)

print(max_people)