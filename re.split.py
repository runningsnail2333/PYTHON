import re
a = [ ]
for i in range(5):
    a = a.append(re.split("\d+","one1two2"))

print(a)
