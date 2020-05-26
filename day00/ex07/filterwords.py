import sys
import string


if len(sys.argv) != 3:
    print("ERROR")
    exit()
a1 = sys.argv[1]
b = a1.maketrans('', '', string.punctuation)
a1 = a1.translate(b)
data = a1.split()

for words in data:
    if not words.isalpha():
        print("ERROR")
        exit()
try:
    a2 = int(sys.argv[2])
except ValueError:
    print("ERROR")
result = []
for words in data:
    if len(words) >= a2:
        result.append(words)
print(result)
