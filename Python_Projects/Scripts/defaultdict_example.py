## Examples of using the collections library defaultdict

# Import
from collections import defaultdict

# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

"""
# Using defaultdict
d = defaultdict(list)
for k, v in s:
	d[k].append(v)
"""

"""
# Default way using standard dictionary
d = {}
for k, v in s:
	d.setdefault(k, []).append(v)
"""

s = 'mississippi'
d = defaultdict(int)
for k in s:
	d[k] += 1

print(d.items())
