# import matplotlib.pyplot as plt

# # Data for each height
# distance = [0, 1.41, 2.82, 4.24, 5.65, 6.40, 7.07, 8.48]

# # Voltage data for each height (in volts)
# transmitter_voltages_0 = [4.96, 4.93, 4.95, 4.92, 4.87, 4.90, 4.98, 5.02]
# receiver_voltages_0 = [4.36, 4.44, 4.26, 5.09, 5.08, 3.78, 1.03, 0]

# transmitter_voltages_3 = [4.92, 4.92, 4.91, 4.88, 4.91, 4.96, 5.02]
# receiver_voltages_3 = [5.08, 5.09, 5.09, 5.08, 3.87, 2.05, 0]

# transmitter_voltages_6 = [4.88, 4.90, 4.93, 4.96, 5.01]
# receiver_voltages_6 = [4.94, 4.07, 3.44, 2.50, 0]

# transmitter_voltages_7 = [4.94, 4.95, 4.98, 5.00, 5.02]
# receiver_voltages_7 = [2.63, 2.22, 1.33, 0.40, 0]

# transmitter_voltages_10 = [4.97, 4.98, 4.99, 5.01]
# receiver_voltages_10 = [1.30, 1.04, 0.20, 0]

# # Create the plot
# plt.figure(figsize=(10, 6))

# # Plot for each height with appropriate labels
# plt.plot(distance, transmitter_voltages_0, label='Transmitter Line (H = 0 mm)', color='blue', marker='o')
# plt.plot(distance, receiver_voltages_0, label='Receiver Line (H = 0 mm)', color='blue', linestyle='--', marker='x')

# plt.plot(distance[:7], transmitter_voltages_3, label='Transmitter Line (H = 3 mm)', color='green', marker='o')
# plt.plot(distance[:7], receiver_voltages_3, label='Receiver Line (H = 3 mm)', color='green', linestyle='--', marker='x')

# plt.plot(distance[:5], transmitter_voltages_6, label='Transmitter Line (H = 6 mm)', color='red', marker='o')
# plt.plot(distance[:5], receiver_voltages_6, label='Receiver Line (H = 6 mm)', color='red', linestyle='--', marker='x')

# plt.plot(distance[:5], transmitter_voltages_7, label='Transmitter Line (H = 7 mm)', color='orange', marker='o')
# plt.plot(distance[:5], receiver_voltages_7, label='Receiver Line (H = 7 mm)', color='orange', linestyle='--', marker='x')

# plt.plot(distance[:4], transmitter_voltages_10, label='Transmitter Line (H = 10 mm)', color='purple', marker='o')
# plt.plot(distance[:4], receiver_voltages_10, label='Receiver Line (H = 10 mm)', color='purple', linestyle='--', marker='x')

# # Adding labels and title
# plt.title('Transmitter and Receiver Coil Voltage vs. Distance')
# plt.xlabel('Distance (D) [mm]')
# plt.ylabel('Voltage (V)')
# plt.legend()
# plt.grid(True)

# # Show the plot
# plt.tight_layout()
# plt.show()



# import matplotlib.pyplot as plt

# # Data for current (mA) at different heights
# distance = [0, 1.41, 2.82, 4.24, 5.65, 6.40, 7.07, 8.48]

# # Current data for each height (in mA)
# transmitter_currents_0 = [343, 342, 318, 401, 467, 412, 268, 194]
# receiver_currents_0 = [158, 164, 133, 122, 143, 119, 53, 0]

# transmitter_currents_3 = [398, 395, 397, 446, 398, 281, 178]
# receiver_currents_3 = [170, 172, 144, 157, 107, 96, 0]

# transmitter_currents_6 = [457, 424, 366, 306, 205]
# receiver_currents_6 = [148, 120, 88, 127, 0]

# transmitter_currents_7 = [335, 315, 267, 236, 180]
# receiver_currents_7 = [117, 102, 68, 42, 0]

# transmitter_currents_10 = [283, 267, 233, 192]
# receiver_currents_10 = [62, 57, 35, 0]

# # Create the plot
# plt.figure(figsize=(10, 6))

# # Plot for each height with appropriate labels
# plt.plot(distance, transmitter_currents_0, label='Transmitter Line (H = 0 mm)', color='blue', marker='o')
# plt.plot(distance, receiver_currents_0, label='Receiver Line (H = 0 mm)', color='blue', linestyle='--', marker='x')

# plt.plot(distance[:7], transmitter_currents_3, label='Transmitter Line (H = 3 mm)', color='green', marker='o')
# plt.plot(distance[:7], receiver_currents_3, label='Receiver Line (H = 3 mm)', color='green', linestyle='--', marker='x')

# plt.plot(distance[:5], transmitter_currents_6, label='Transmitter Line (H = 6 mm)', color='red', marker='o')
# plt.plot(distance[:5], receiver_currents_6, label='Receiver Line (H = 6 mm)', color='red', linestyle='--', marker='x')

# plt.plot(distance[:5], transmitter_currents_7, label='Transmitter Line (H = 7 mm)', color='orange', marker='o')
# plt.plot(distance[:5], receiver_currents_7, label='Receiver Line (H = 7 mm)', color='orange', linestyle='--', marker='x')

# plt.plot(distance[:4], transmitter_currents_10, label='Transmitter Line (H = 10 mm)', color='purple', marker='o')
# plt.plot(distance[:4], receiver_currents_10, label='Receiver Line (H = 10 mm)', color='purple', linestyle='--', marker='x')

# # Adding labels and title
# plt.title('Transmitter and Receiver Coil Current vs. Distance')
# plt.xlabel('Distance (D) [mm]')
# plt.ylabel('Current (mA)')
# plt.legend()
# plt.grid(True)

# # Show the plot
# plt.tight_layout()
# plt.show()



# import matplotlib.pyplot as plt

# # Data for power calculation
# distance = [0, 1.41, 2.82, 4.24, 5.65, 6.40, 7.07, 8.48]

# # Voltage (V) data for each height
# transmitter_voltages_0 = [4.96, 4.93, 4.95, 4.92, 4.87, 4.90, 4.98, 5.02]
# receiver_voltages_0 = [4.36, 4.44, 4.26, 5.09, 5.08, 3.78, 1.03, 0]

# transmitter_voltages_3 = [4.92, 4.92, 4.91, 4.88, 4.91, 4.96, 5.02]
# receiver_voltages_3 = [5.08, 5.09, 5.09, 5.08, 3.87, 2.05, 0]

# transmitter_voltages_6 = [4.88, 4.90, 4.93, 4.96, 5.01]
# receiver_voltages_6 = [4.94, 4.07, 3.44, 2.50, 0]

# transmitter_voltages_7 = [4.94, 4.95, 4.98, 5.00, 5.02]
# receiver_voltages_7 = [2.63, 2.22, 1.33, 0.40, 0]

# transmitter_voltages_10 = [4.97, 4.98, 4.99, 5.01]
# receiver_voltages_10 = [1.30, 1.04, 0.20, 0]

# # Current (mA) data for each height
# transmitter_currents_0 = [343, 342, 318, 401, 467, 412, 268, 194]
# receiver_currents_0 = [158, 164, 133, 122, 143, 119, 53, 0]

# transmitter_currents_3 = [398, 395, 397, 446, 398, 281, 178]
# receiver_currents_3 = [170, 172, 144, 157, 107, 96, 0]

# transmitter_currents_6 = [457, 424, 366, 306, 205]
# receiver_currents_6 = [148, 120, 88, 127, 0]

# transmitter_currents_7 = [335, 315, 267, 236, 180]
# receiver_currents_7 = [117, 102, 68, 42, 0]

# transmitter_currents_10 = [283, 267, 233, 192]
# receiver_currents_10 = [62, 57, 35, 0]

# # Power calculation (Power = Voltage * Current)
# def calculate_power(voltage, current):
#     return [v * i for v, i in zip(voltage, current)]

# # Calculate power for each height
# transmitter_power_0 = calculate_power(transmitter_voltages_0, transmitter_currents_0)
# receiver_power_0 = calculate_power(receiver_voltages_0, receiver_currents_0)

# transmitter_power_3 = calculate_power(transmitter_voltages_3, transmitter_currents_3)
# receiver_power_3 = calculate_power(receiver_voltages_3, receiver_currents_3)

# transmitter_power_6 = calculate_power(transmitter_voltages_6, transmitter_currents_6)
# receiver_power_6 = calculate_power(receiver_voltages_6, receiver_currents_6)

# transmitter_power_7 = calculate_power(transmitter_voltages_7, transmitter_currents_7)
# receiver_power_7 = calculate_power(receiver_voltages_7, receiver_currents_7)

# transmitter_power_10 = calculate_power(transmitter_voltages_10, transmitter_currents_10)
# receiver_power_10 = calculate_power(receiver_voltages_10, receiver_currents_10)

# # Create the plot
# plt.figure(figsize=(10, 6))

# # Plot for each height with appropriate labels
# plt.plot(distance, transmitter_power_0, label='Transmitter Power Line (H = 0 mm)', color='blue', marker='o')
# plt.plot(distance, receiver_power_0, label='Receiver Power Line (H = 0 mm)', color='blue', linestyle='--', marker='x')

# plt.plot(distance[:7], transmitter_power_3, label='Transmitter Power Line (H = 3 mm)', color='green', marker='o')
# plt.plot(distance[:7], receiver_power_3, label='Receiver Power Line (H = 3 mm)', color='green', linestyle='--', marker='x')

# plt.plot(distance[:5], transmitter_power_6, label='Transmitter Power Line (H = 6 mm)', color='red', marker='o')
# plt.plot(distance[:5], receiver_power_6, label='Receiver Power Line (H = 6 mm)', color='red', linestyle='--', marker='x')

# plt.plot(distance[:5], transmitter_power_7, label='Transmitter Power Line (H = 7 mm)', color='orange', marker='o')
# plt.plot(distance[:5], receiver_power_7, label='Receiver Power Line (H = 7 mm)', color='orange', linestyle='--', marker='x')

# plt.plot(distance[:4], transmitter_power_10, label='Transmitter Power Line (H = 10 mm)', color='purple', marker='o')
# plt.plot(distance[:4], receiver_power_10, label='Receiver Power Line (H = 10 mm)', color='purple', linestyle='--', marker='x')

# # Adding labels and title
# plt.title('Transmitter and Receiver Coil Power vs. Distance')
# plt.xlabel('Distance (D) [mm]')
# plt.ylabel('Power (mW)')
# plt.legend()
# plt.grid(True)

# # Show the plot
# plt.tight_layout()
# plt.show()


import matplotlib.pyplot as plt

# Data for distances
distance = [0, 1.41, 2.82, 4.24, 5.65, 6.40, 7.07, 8.48]

# Voltage (V) data for each height
transmitter_voltages_0 = [4.96, 4.93, 4.95, 4.92, 4.87, 4.90, 4.98, 5.02]
receiver_voltages_0 = [4.36, 4.44, 4.26, 5.09, 5.08, 3.78, 1.03, 0]

transmitter_voltages_3 = [4.92, 4.92, 4.91, 4.88, 4.91, 4.96, 5.02]
receiver_voltages_3 = [5.08, 5.09, 5.09, 5.08, 3.87, 2.05, 0]

transmitter_voltages_6 = [4.88, 4.90, 4.93, 4.96, 5.01]
receiver_voltages_6 = [4.94, 4.07, 3.44, 2.50, 0]

transmitter_voltages_7 = [4.94, 4.95, 4.98, 5.00, 5.02]
receiver_voltages_7 = [2.63, 2.22, 1.33, 0.40, 0]

transmitter_voltages_10 = [4.97, 4.98, 4.99, 5.01]
receiver_voltages_10 = [1.30, 1.04, 0.20, 0]

# Current (mA) data for each height
transmitter_currents_0 = [343, 342, 318, 401, 467, 412, 268, 194]
receiver_currents_0 = [158, 164, 133, 122, 143, 119, 53, 0]

transmitter_currents_3 = [398, 395, 397, 446, 398, 281, 178]
receiver_currents_3 = [170, 172, 144, 157, 107, 96, 0]

transmitter_currents_6 = [457, 424, 366, 306, 205]
receiver_currents_6 = [148, 120, 88, 127, 0]

transmitter_currents_7 = [335, 315, 267, 236, 180]
receiver_currents_7 = [117, 102, 68, 42, 0]

transmitter_currents_10 = [283, 267, 233, 192]
receiver_currents_10 = [62, 57, 35, 0]

# Function to calculate power (mW)
def calculate_power(voltage, current):
    return [v * i for v, i in zip(voltage, current)]

# Calculate power for each height
transmitter_power_0 = calculate_power(transmitter_voltages_0, transmitter_currents_0)
receiver_power_0 = calculate_power(receiver_voltages_0, receiver_currents_0)

transmitter_power_3 = calculate_power(transmitter_voltages_3, transmitter_currents_3)
receiver_power_3 = calculate_power(receiver_voltages_3, receiver_currents_3)

transmitter_power_6 = calculate_power(transmitter_voltages_6, transmitter_currents_6)
receiver_power_6 = calculate_power(receiver_voltages_6, receiver_currents_6)

transmitter_power_7 = calculate_power(transmitter_voltages_7, transmitter_currents_7)
receiver_power_7 = calculate_power(receiver_voltages_7, receiver_currents_7)

transmitter_power_10 = calculate_power(transmitter_voltages_10, transmitter_currents_10)
receiver_power_10 = calculate_power(receiver_voltages_10, receiver_currents_10)

# Function to calculate efficiency
def calculate_efficiency(receiver_power, transmitter_power):
    return [(rp / tp * 100) if tp != 0 else 0 for rp, tp in zip(receiver_power, transmitter_power)]

# Calculate efficiency for each height
efficiency_0 = calculate_efficiency(receiver_power_0, transmitter_power_0)
efficiency_3 = calculate_efficiency(receiver_power_3, transmitter_power_3)
efficiency_6 = calculate_efficiency(receiver_power_6, transmitter_power_6)
efficiency_7 = calculate_efficiency(receiver_power_7, transmitter_power_7)
efficiency_10 = calculate_efficiency(receiver_power_10, transmitter_power_10)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot efficiency for each height
plt.plot(distance, efficiency_0, label='Efficiency (H = 0 mm)', color='blue', marker='o')
plt.plot(distance[:7], efficiency_3, label='Efficiency (H = 3 mm)', color='green', marker='o')
plt.plot(distance[:5], efficiency_6, label='Efficiency (H = 6 mm)', color='red', marker='o')
plt.plot(distance[:5], efficiency_7, label='Efficiency (H = 7 mm)', color='orange', marker='o')
plt.plot(distance[:4], efficiency_10, label='Efficiency (H = 10 mm)', color='purple', marker='o')

# Adding labels and title
plt.title('Efficiency vs. Distance for Different Heights')
plt.xlabel('Distance (D) [mm]')
plt.ylabel('Efficiency (%)')
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

