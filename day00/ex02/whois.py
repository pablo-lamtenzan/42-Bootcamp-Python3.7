import sys

nb = sys.argv[1]

try:
    nb = int(nb)
    if nb == 0:
        print("I'm Zero.")
    else:
        print("I'm odd.") if not (nb % 2) == 0 else print("I'm even.")
except ValueError:
    print("ERROR")