resistors = []
while True:
    resistor_value = input("Enter resistor value in ohms (or leave empty to finish): ")
    if resistor_value == "":
        break

    resistors.append(float(resistor_value))


configuration = input("Enter configuration (series/parallel): ").lower().strip()
if configuration == "series":
    # the below three lines can also be written in a nicer way as:
    # total_resistance = sum(resistors)
    total_resistance = 0
    for i in resistors:
        total_resistance += i

    print(f"The total resistance for series resistors is: {total_resistance} ohms")

elif configuration == "parallel":
    # the below three lines can also be written in a nicer way as:
    # reciprocal_sum = sum(1 / r for r in resistors)
    reciprocal_sum = 0
    for i in resistors:
        reciprocal_sum += 1 / i

    total_resistance = 1 / reciprocal_sum
    print(f"The total resistance for parallel resistors is: {total_resistance} ohms")

else:
    print("Invalid configuration. Please enter either 'series' or 'parallel'.")
