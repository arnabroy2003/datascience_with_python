import numpy as np
x = [8,10,12]
y = [10,13,16]

x_array = np.array(x)
y_array = np.array(y)

x_mean = int(np.mean(x_array))
y_mean = int(np.mean(y_array))

deviations_x = []
deviations_y = []

for i in x:
    deviations_x.append(i-x_mean)
for i in y:
    deviations_y.append(i-y_mean)

sum_of_product_of_deviations = 0

for i in range(len(x)):
    sum_of_product_of_deviations = sum_of_product_of_deviations + (deviations_x[i] * deviations_y[i])

sum_of_square_of_deviations_for_x = 0
for i in deviations_x:
    sum_of_square_of_deviations_for_x = sum_of_square_of_deviations_for_x + (deviations_x[i]**2)

m = sum_of_product_of_deviations/sum_of_square_of_deviations_for_x
b = y_mean-(m*x_mean)

new_x = 20

predict_y = m*new_x+b
print(f"Expected price will be ${predict_y}")