flag = True
l1 = []

while (flag):
    inp = int(input())
    if inp != 0:
        l1.append(inp)
    else:
        break

print(list(reversed(sorted(l1))))
