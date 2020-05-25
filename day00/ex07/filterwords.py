import sys

if len(sys.argv) != 3:
    print("ERROR")
    exit()
try:
    a1 = sys.argv[1].isalpha()  # ???????????
except ValueError:
    print("ERROR")
try:
    a2 = int(sys.argv[2])
except ValueError:
    print("ERROR")
# some split
# loop in every entity of the split
# check the lenght then compare it to a2
# if is < del it
# then start another time and remove pontuation ex02
# print the result tensor

