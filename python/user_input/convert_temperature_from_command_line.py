  Temperature data
    ----------------
    Fahrenheit degrees: 67.2
    Fahrenheit degrees: 66.0
    Fahrenheit degrees: 78.9
    Fahrenheit degrees: 102.1
    Fahrenheit degrees: 32.0
    Fahrenheit degrees: 87.8


    def fahrenheit_to_celsius(fahrenheit_temp):
    """
    Converts a temperature from Fahrenheit to Celsius using the formula:
    C = (°F - 32) / 1.8
    """


    celsius_temp = (fahrenheit_temp - 32) / 1.8
    return celsius_temp

if __name__ == '__main__':
   
    try:
    
    
        input_fahrenheit = float(input("Please enter the temperature in Fahrenheit degrees: "))

   
        output_celsius = fahrenheit_to_celsius(input_fahrenheit)


        print(f"The input temperature of {input_fahrenheit:.2f} degrees Fahrenheit is equal to {output_celsius:.2f} degrees Celsius.")


        
    except ValueError:

        print("Invalid input! Please enter a valid number for the temperature.")