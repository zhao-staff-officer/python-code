s = 0
i = 1
while i <= 100:
    if i % 2 == 1:
        i += 1
        continue
    s += i
    i += 1
print(s)

s2 = 0
for i in range(1, 101):
    if i % 2 == 1:
        continue
    s2 += i
print(s2)
