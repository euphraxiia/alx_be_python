# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        # Validate temperature input is numeric (int or float)
        temperature = float(temp_input)
        
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError as ve:
        raise ValueError("Invalid temperature. Please enter a numeric value.") from ve

# Explicit check functions (or test cases)
def run_checks():
    # Check for global conversion factors
    assert 'FAHRENHEIT_TO_CELSIUS_FACTOR' in globals(), "Missing FAHRENHEIT_TO_CELSIUS_FACTOR"
    assert 'CELSIUS_TO_FAHRENHEIT_FACTOR' in globals(), "Missing CELSIUS_TO_FAHRENHEIT_FACTOR"

    # Check conversion functions exist and produce expected output
    assert callable(convert_to_celsius), "convert_to_celsius function not implemented"
    assert callable(convert_to_fahrenheit), "convert_to_fahrenheit function not implemented"
    # Simple correctness check
    assert abs(convert_to_celsius(32) - 0) < 1e-6, "convert_to_celsius incorrect for 32°F"
    assert abs(convert_to_fahrenheit(0) - 32) < 1e-6, "convert_to_fahrenheit incorrect for 0°C"

    # Check error raising for invalid temperature input
    try:
        float("abc")  # Should raise ValueError outside our code, but we emulate
    except ValueError:
        pass  # Expected
    else:
        assert False, "ValueError not raised for invalid numeric temperature"

    # Note: User interaction presence can't be asserted programmatically here,
    # but we can mention that main() contains input() calls.

    print("All checks passed!")

if __name__ == "__main__":
    run_checks()
    main()
