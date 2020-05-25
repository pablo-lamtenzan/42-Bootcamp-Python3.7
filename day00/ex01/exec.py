import sys

print(' '.join(sys.argv[1::]).swapcase()[::-1]) if sys.argv().len() > 1 else 0