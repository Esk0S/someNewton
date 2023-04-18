import math

with open('Interpolation/test_04.txt') as f:
    xs = [float(i) for i in f.readline()[3:-1].split(' ')]
    ys = [float(i) for i in f.readline()[3:-1].split(' ')]
    f.readline()
    x = float(f.readline()[4:])
    f.close()

dy = [[], []]
dy[0] = ys.copy()
dyLen = len(ys)
for i in range(1, dyLen):
    dy.insert(i, [round(dy[i - 1][j + 1] - dy[i - 1][j], 4) for j in range(0, len(dy[i - 1]) - 1)])
    dyLen -= 1
q = (x-xs[0])/(xs[1] - xs[0])
k = 1
y = dy[0][0]
for i in range(len(ys) - 1):
    xxx = 1
    for j in range(1, k):
        xxx *= q - j
    y += (dy[k][0]/math.factorial(k)) * q * xxx
    k += 1

for i in dy:
    for j in i:
        print(j, end=' ')
    print()

print(y)
