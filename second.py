d1 = {'Dangenov': (28, 'gg@.com'), 'Masterov': (14, 'rr@.com')}
date = int(input())

for i in d1.keys():
    if d1[i][0] > date and date < 31:
        print(i)