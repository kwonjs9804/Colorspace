a = [1, 2, 3, 4, 5, 6, 7, 8]
c = 0
for i in range(0, len(a)-1):
    sum = 0
    b = (a[i] + a[i+1])/2
    sum = sum + b
    c = c + sum
print(c)
