def fahrenheit_to_celsius(f):
    """Converts a Fahrenheit temperature to Celsius."""
    # Formula: C = (F - 32) * 5/9
    c = (f - 32.0) * (5.0 / 9.0)
    return round(c, 1) # Round to one decimal place

# --- Example Usage ---
temp_f = 68.0
temp_c = fahrenheit_to_celsius(temp_f)
print(f"\n{temp_f}°F is equal to {temp_c}°C") # Output: 20.0°C
