import random, datetime, string
import numpy as np
import math

target = "14h!S@A$Qse35DAzx"
character = string.ascii_letters + string.punctuation
k = len(target)
char = len(character)

length = np.array([12, 14, 16, 18, 20, 22, 24, 26])  # Array of lengths
duration = []  # List to store durations

# Measuring the time for random string generation at various lengths
print("\nProcessing......")
for l in length:
    start = datetime.datetime.now()
    for _ in range(10**6):
        s = ''.join(random.choice(character) for _ in range(l))
    end = datetime.datetime.now()
    temp = end - start
    duration.append(temp.total_seconds())

duration = np.array(duration)
print("Done inputting duration")

# Linear function definition
def f(x, phi0, phi1):
    return phi0 + phi1 * x

# Compute the loss function
def compute_loss(x, y, phi0, phi1):
    y_pred = f(x, phi0, phi1)
    error = y_pred - y
    loss = sum(error * error)
    return loss

# Data for linear regression
x_train = length
y_train = duration

# Calculate the values of phi0 and phi1 using least squares method
sum_x = sum(x_train)
sum_y = sum(y_train)
sum_xy = sum(x_train * y_train)
sum_x2 = sum(x_train * x_train)
T = len(x_train)

# Linear regression coefficients
top = (T * sum_xy - sum_x * sum_y)
bottom = (T * sum_x2 - sum_x * sum_x)
phi1 = top / bottom
phi0 = sum_y / T - phi1 * sum_x / T

# Print the linear regression coefficients and loss
print(f"Predicted duration = {phi0} + {phi1} * length")
print("Loss:", compute_loss(x_train, y_train, phi0, phi1))

# Predict the time for a string of length k
predicted_time = f(k, phi0, phi1)
passwordPerSecond = 10**6 / predicted_time

# Estimated brute-force attempts
counter = 5
failure = math.floor(passwordPerSecond / counter)
wasted = 5
total_wasted = wasted * failure
total_gen = char ** k

# Estimating time in years
est_time = (total_gen / passwordPerSecond + total_wasted) / 3.15576e+7
print(f"Total generations: \t{total_gen}")
print(f"Estimated time:  \t{est_time} years (approximate)\n")
