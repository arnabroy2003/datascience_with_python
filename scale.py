# Standard scale (z)
# z = (x-mean)/standard deviation
import math

x = [2,6,3,5,4]
n = len(x)
sum = 0
sigma = 0

#Calculate Mean
for i in range(n):
    sum = sum + x[i]
mean = sum/n

#Calculate Standard Deviation
for j in range(n):
    sigma = sigma + ((x[j] - mean)**2)

s_d = math.sqrt(sigma/n)

#Calculate Scale
for scale in x:
    scale_value = (scale-mean)/s_d
    print(scale_value)
