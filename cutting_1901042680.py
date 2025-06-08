import math

def cutting(a):
    return cut(a, 0)
    
def cut(left, right):
    if left == 1 and right == 0:
        return 0
    elif right == 0 and left != 1:
        return 1 + cut(left//2, left - left//2)
    elif left == 1 and right != 1:
        return 1 + cut(right//2, right - right//2)
    elif left == 1 and right == 1:
        return 0
    else:
        return 1 + cut(math.ceil(left/2), math.ceil(right/2))

for i in range(1, 34):
    print("min number of cuts for ", i, ": ", cutting(i))