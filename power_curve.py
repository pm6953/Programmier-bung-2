from load_data import load_data
from sort import bubble_sort
from matplotlib import pyplot as plt

time_data = load_data('activity.csv')
time_array = time_data['Duration']

data = load_data('activity.csv')
power_W = data['PowerOriginal']
print(power_W)
sorted_power_W = bubble_sort(power_W)
print(sorted_power_W[::-1])

plt.plot(sorted_power_W[::-1])
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.title('Power Curve')
plt.grid()
plt.show()
