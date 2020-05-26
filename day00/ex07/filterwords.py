import sys
import string

if len(sys.argv) != 3:
    print("ERROR")
    exit()
if any(char.isalpha() for char in sys.argv[1]) and any(char.isspace() for char in sys.argv[1]):
    a1 = sys.argv[1]
else:
    print("ERROR")
    exit()
try:
    a2 = int(sys.argv[2])
except ValueError:
    print("ERROR")
i = 0
result = {}
data = a1.split()
for words in data:
    if len(words) >= a2:
        result[i] = words
        i += 1

print(result)
"""
print("[", end='')
for i in result:
    print("'%s'%c" % (result[i], ',' if (i < len(result) else ''), end='')
print("]")
"""
# remove last coma and is ok
# add poctuation to parse and remove it later