a = input()
b = a.split()

wordlens = [(len(word), word) for word in b]
wordlens.sort()

c= min (wordlens)
print(c[0])
