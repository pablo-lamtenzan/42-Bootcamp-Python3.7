import sys

print(' '.join(sys.argv[1::]).swapcase()[::-1]) if len(sys.argv > 1 else 0