# Given a positive integer, decompose it into sum of m consecutive positive integers, output solution with minimum m

# Assume m positive integers: smallest is x, then:
# x + (x+1) + (x+2) + ... + (x+m-1) = n
# i.e., m*x + (1+2+...+(m-1)) = n
# i.e., m*x + m*(m-1)/2 = n
# i.e., m*x = n - m*(m-1)/2
# i.e., x = (n - m*(m-1)/2) / m
# Since x is positive integer, n - m*(m-1)/2 must be > 0 and divisible by m
# Increase m from 2, until n - m*(m-1)/2 <= 0
# If cannot decompose, output 'N'

# Output expression

n = int(input())
m = 2
found = False
while True:
    remainder = n - m * (m - 1) // 2
    if remainder <= 0:
        break
    if remainder % m == 0:
        x = remainder // m
        if x > 0:
            found = True
            result = '+'.join(str(x + i) for i in range(m))
            break
    m += 1

if not found:
    print('N')
else:
    print(f"{n}=" + result)