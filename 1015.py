import math
x1,y1 = input().split()
x2,y2 = input().split()
a = math.sqrt(((float(x2)-float(x1))*(float(x2)-float(x1))) +((float(y2)-float(y1))*(float(y2)-float(y1))))
print("%0.4f"%a)
