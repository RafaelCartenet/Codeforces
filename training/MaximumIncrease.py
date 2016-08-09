n = int(input())
l = list(map(int,input().split()))

ma = 1
m = 1
for i in range(n - 1):
    if l[i+1] > l[i]:
        m += 1
        ma = max(m, ma)
    else:
        m = 1
print(ma)
