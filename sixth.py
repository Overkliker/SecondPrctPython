flag = True
l1 = []

while (flag):
    try:
        inp = int(input())
        l1.append(inp)
    except ValueError:
        break


print('\t'.join(map(lambda x: str(x), sorted(l1))))
