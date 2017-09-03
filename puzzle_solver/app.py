a = []
b = []
for i in range(1, 19):
    for j in range(1, 10):
        for k in range(1, 7):
            if i != j and i != k and j != k:
                if i*j*k == 36:
                    a.append([i, j, k])
for h in range(len(a)):
    a[h].sort()
a.sort()
#print(a)

for g in range(1, len(a)):
    if a[g] != a[g-1]:
        b.append(a[g-1])
b.append(a[g])
print(b)
print(sum(b[0]), sum(b[1]), sum(b[2]), sum(b[3]))