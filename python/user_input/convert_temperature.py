import sys

def convert_temperature():
    if len(sys.argv) != 3:
        print("Usage: python convert_temperature.py <temperature> <unit>")
        print("Example: python convert_temperature.py 25 C")
        return
    
    try:
        temp = float(sys.argv[1])
        unit = sys.argv[2].upper()
        
        if unit == 'C':
            f = (temp * 9/5) + 32
            k = temp + 273.15
            print(f"{temp}°C = {f:.2f}°F = {k:.2f}K")
        elif unit == 'F':
            c = (temp - 32) * 5/9
            k = c + 273.15
            print(f"{temp}°F = {c:.2f}°C = {k:.2f}K")
        elif unit == 'K':
            if temp < 0:
                print("Error: Kelvin cannot be negative!")
                return
            c = temp - 273.15
            f = (c * 9/5) + 32
            print(f"{temp}K = {c:.2f}°C = {f:.2f}°F")
        else:
            print("Error: Use C, F, or K for unit")
            
    except ValueError:
        print("Error: Please enter a valid number")

if __name__ == "__main__":
    convert_temperature()