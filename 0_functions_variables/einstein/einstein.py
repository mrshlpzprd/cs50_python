# Prompt user to enter mass in kilograms
mass = int(input('Please enter the mass in kg: '))

# Print the result of E in Joules
speed_of_light = 300000000
energy = mass * pow(speed_of_light, 2)
print(energy)
