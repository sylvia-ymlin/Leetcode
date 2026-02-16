# Statistical Top N visited pages
# Input
# Each line is a URL or a number. If it is a URL, it represents a web access within a period
# If it is a number N, it represents outputting Top N URLs (count results of all previous URL accesses before current number)

# Total web pages less than 5000, single page access count less than 65535 -> Data volume not large, can use dictionary
# Web URL consists of digits, dots, length less than 127 bytes
# Number is positive integer, less than or equal to 10 and less than current total accessed pages

# For each input number N, output Top N URLs based on current access counts

from collections import defaultdict

# Cannot print in advance, will break input stream
res = []
try:
    counts = defaultdict(int)
    while True:
        line = input().strip()
        if line.isdigit():
            N = int(line)
            # Output Top N URLs based on current access counts
            sorted_urls = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            top_n_urls = [url for url, count in sorted_urls[:N]]
            res.append(','.join(top_n_urls))
        else:
            counts[line] += 1
except EOFError:
    pass

for output in res:
    print(output)
