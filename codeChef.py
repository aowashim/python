from collections import defaultdict
li = [100, 300, 50, 100, 50, 5, 5, 5, 60, 60]
d = defaultdict(int)
for i in li:
    d[i] += 1

print(d.keys())