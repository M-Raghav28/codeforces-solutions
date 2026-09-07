n = int(input())

previous = ""
groups = 0

for _ in range(n):
    magnet = input()

    if magnet != previous:
        groups += 1

    previous = magnet

print(groups)