def add(x1, y1):
    return x1 + y1

def subtract(x2, y2):
    return abs(x2-y2)

x = 1
y = 2

print("This is the sum {x}, {y}, {sum}".format(x=x, y=y, sum=add(x, y)))
print("This is the difference {x}, {y}, {diff}".format(x=x, y=y, diff=subtract(x, y)))
