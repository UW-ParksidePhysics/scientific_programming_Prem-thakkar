import sys

# Check if command line argument is provided
if len(sys.argv) != 2:
    print("Usage: python convert_fahrenheit_temperature_to_celsius_from_command_line.py <temperature>")
    print("Example: python convert_fahrenheit_temperature_to_celsius_from_command_line.py 98.6")
    sys.exit(1)

# Read Fahrenheit temperature from command line
try:
    fahrenheit = float(sys.argv[1])
    
    # Convert to Celsius
    celsius = (fahrenheit - 32) * 5/9
    
    # Print both temperatures
    print(f"{fahrenheit}°F = {celsius}°C")
    
except ValueError:
    print("Error: Please enter a valid number")
    sys.exit(1)