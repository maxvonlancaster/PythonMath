import matplotlib.pyplot as plt
import math

def funcSinDiv(x):
    return math.sin(math.pi / x)

def funcPower(x, n):
    return math.pow(x, n)

points_x = []
points_y = []
points_y_2 = []
points_y_3 = []
points_y_4 = []
points_y_5 = []
points_y_6 = []
points_y_7 = []
points_y_8 = []
points_y_9 = []
points_y_10 = []
points_y_11 = []

#interval = 0.001
#start = -5.0005
#n = 10000

interval = 0.001
start = 0
n = 1000

for i in range(n):
    x = start + i*interval
    points_x.append(x)
    #points_y.append(funcSinDiv(x))
    points_y_2.append(funcPower(x, 2))
    points_y_3.append(funcPower(x, 3))
    points_y_4.append(funcPower(x, 4))
    points_y_5.append(funcPower(x, 5))
    points_y_6.append(funcPower(x, 6))
    points_y_7.append(funcPower(x, 7))
    points_y_8.append(funcPower(x, 8))
    points_y_9.append(funcPower(x, 9))
    points_y_10.append(funcPower(x, 10))
    points_y_11.append(funcPower(x, 11))
    points_y.append(x)

    

plt.plot(points_x,points_y, color='b', linewidth=1.0)
plt.plot(points_x,points_y_2, color='b', linewidth=1.0)
plt.plot(points_x,points_y_3, color='b', linewidth=1.0)
plt.plot(points_x,points_y_4, color='b', linewidth=1.0)
plt.plot(points_x,points_y_5, color='b', linewidth=1.0)
plt.plot(points_x,points_y_6, color='b', linewidth=1.0)
plt.plot(points_x,points_y_7, color='b', linewidth=1.0)
plt.plot(points_x,points_y_8, color='b', linewidth=1.0)
plt.plot(points_x,points_y_9, color='b', linewidth=1.0)
plt.plot(points_x,points_y_10, color='b', linewidth=1.0)
plt.plot(points_x,points_y_11, color='b', linewidth=1.0)

plt.show()
