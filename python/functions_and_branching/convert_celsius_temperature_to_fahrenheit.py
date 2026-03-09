def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
    return (9./5)*celsius_temperature + 32


def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
    return (5./9) * (fahrenheit_temperature - 32)


freezing_point_of_water_celsius = 0.
print(f'Freezing point of water in Celsius:')
print(f'{convert_fahrenheit_temperature_to_celsius(convert_celsius_temperature_to_fahrenheit(freezing_point_of_water_celsius))} = {freezing_point_of_water_celsius}')
print()

room_temperature_celsius = 21.
print(f'Room temperature in Celsius:')
print(f'{convert_fahrenheit_temperature_to_celsius(convert_celsius_temperature_to_fahrenheit(room_temperature_celsius))} = {room_temperature_celsius}')
print()

boiling_point_of_water_celsius = 100.
print(f'Boiling point of water in Celsius:')
print(f'{convert_fahrenheit_temperature_to_celsius(convert_celsius_temperature_to_fahrenheit(boiling_point_of_water_celsius))} = {boiling_point_of_water_celsius}')
print()