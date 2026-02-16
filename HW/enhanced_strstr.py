"""
2025-10-22 L3

Enhanced character search, select optional fields, perform fuzzy search
"""

import sys

# Read input
source = sys.stdin.readline().strip()
pattern = sys.stdin.readline().strip()

result = -1

fixed_parts = pattern.split('[')[0]

if fixed_parts in source: result = source.index(fixed_parts)

remaining = pattern.split('[')[1].rstrip(']')

for x in remaining:
    if fixed_parts + x in source:
        result = source.index(fixed_parts + x)
        break

print(result)
