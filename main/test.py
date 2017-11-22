a = [11, 21, 31, 41]
b = (1,2,3)
c = list(b)
c.sort(key=lambda x:-x)
print(c)