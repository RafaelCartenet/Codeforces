n = int(input())

w = ["I hate ", "I love "]

res = ""
for i in range(n):
    res += w[i % 2]
    if i < n-1:
        res += "that "
    else:
        res += "it"

print(res)
