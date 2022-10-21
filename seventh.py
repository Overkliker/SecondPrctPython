def reverse_lookup(d1, word):
    return list(map(lambda y: y[0], filter(lambda x: x[1] == word, d1.items())))


print(reverse_lookup({'gg': 123, "ll": 456, 'dd': 123}, 123))
print(reverse_lookup({}, 123))
