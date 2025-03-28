N = int(input())
people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

ranks = []
for i in range(N):
    count = 0
    for j in range(N):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            count += 1
    ranks.append(count + 1)

print(' '.join(map(str, ranks)))
