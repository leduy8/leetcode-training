from typing import List

# * https://leetcode.com/problems/convert-the-temperature/

# ? Kelvin = Celsius + 273.15
# ? Fahrenheit = Celsius * 1.80 + 32.00

def convertTemperature(celsius: float) -> List[float]:
    return [float(celsius + 273.15),  float(celsius * 1.80 + 32.00)]

print(convertTemperature(celsius = 36.50)) # [309.65000,97.70000]
print(convertTemperature(celsius = 122.11)) # [395.26000,251.79800]
