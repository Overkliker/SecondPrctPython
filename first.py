from collections import Counter


l1 = [('b', 'b', 'a', 1), ('a', 'a', 'a', 21)]

mx = 0
al = ''
ind = 0
d1 = {}

for i in range(len(l1)):
    for j in l1[i]:
        if j not in d1.keys():
            d1[j] = l1[i].count(j)

        elif j in d1.keys() and l1.index(l1[i]) > ind:
            d1[j] += 1

    if ind == 0:
        ind -= 1

    ind += 1

print(max(d1, key=d1.get))

