FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):

    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    
def convert_to_fahrenheit(celsius):    

    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


try:
    temp_to_convert = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()
celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
match celsius_or_fahrenheit:
    case "F":
        print(f"{temp_to_convert}°F is {convert_to_celsius(temp_to_convert)}°C")
        
    case "C":
        print(f"{temp_to_convert}°C is {convert_to_fahrenheit(temp_to_convert)}°F")
        