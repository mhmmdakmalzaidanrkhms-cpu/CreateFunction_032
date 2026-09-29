#cihuyyyy
import math

def convert_temperature(value, unit):
    unit = unit.upper()
    if unit == 'C':
        
        return (value * 9 / 5) + 32
    elif unit == 'F':
       
        return (value - 32) * 5 / 9



