from collections import Counter

# Tally occurences fo words in a list
print(Counter())

print(Counter('gallahad'))

print(Counter({'red': 4, 'blue': 2}))

print(Counter(cats=4, dogs=8))

count = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
	count[word] += 1
print (count)

count2 = Counter(['eggs', 'ham'])
print(count2)
print(count2['bacon'])

count2['eggs'] = 0
print(count2)

del count2['eggs']
print(count2)

# .elements() functionality
e_count = Counter(a=4, b=2, c=0, d=-2)
print(list(e_count.elements()))

# .most_common(n) functionality, returns a list of the n most common elements and their counts
c_count = Counter('abracadabra').most_common(3)
print(c_count)