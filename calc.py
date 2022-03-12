res = 0
for n in range(1, 101):
    res += n ** 3 - n ** (1.0 / 3)
print(res)
