import math
n = int(input())
arr = list(map(int, input().split()))
count = 0
for num in arr:
    if math.floor(math.log10(num)) % 2 == 1:
        count += 1
print(count)