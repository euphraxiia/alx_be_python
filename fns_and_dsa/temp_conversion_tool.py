# temp_conversion_tool.py
# Temperature Conversion Tool demonstrating variable scope with global conversion factors

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius using global conversion factor.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature converted to Celsius
    """
    # Use global conversion factor to convert F to C
    # Formula: (F - 32) * (5/9)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit using global conversion factor.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature converted to Fahrenheit
    """
    # Use global conversion factor to convert C to F
    # Formula: C * (9/5) + 32
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    try:
        # Get temperature input from user
        temp_input = input("Enter the temperature to convert: ")
        
        # Validate temperature input - convert to float
        try:
            temperature = float(temp_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        # Get unit input from user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
        
        # Validate unit input
        if unit not in ['C', 'F']:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            return
        
        # Perform conversion based on unit
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
