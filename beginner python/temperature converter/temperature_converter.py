# Define function with parameters
def temperature_calculator(temperature, input_temperature, output_temperature):
    
    if input_temperature == 'C':
        if output_temperature == 'F':
            # °F = (°C * 9/5) + 32
            return (temperature * 9/5) + 32
        else:
            return temperature

    elif input_temperature == 'F':
        if output_temperature == 'C':
            # °C = (°F - 32) * 5/9
            return (temperature - 32) * 5/9
        else:
            return temperature
    else:
        return temperature

while True:
    # User input temperature and convert output temperature
    temperature = float(input("Enter temperature: "))
    input_temperature = input("Enter input temperature scale C or F: ").upper()
    output_temperature = input("Enter output temperature scale C or F: ").upper()

    # Call function with arguements and print temperature result (°C to °F or °F to °C)
    result = temperature_calculator(temperature, input_temperature, output_temperature)
    print(temperature, input_temperature, "=", result, output_temperature)

