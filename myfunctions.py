# Function to convert decimal degrees to degree minutes and seconds
def degtodms(decimal, decimals=0):
    dd = int(decimal)
    decimal = abs(decimal - dd) * 60
    mm = int(decimal)
    ss = (decimal - mm) * 60
    if mm == 59 and round(ss) == 60:
        dd += 1; mm = 0; ss = 0
    if round(ss) == 60:
        mm += 1; ss = 0
    return f'{dd}° {mm}\' {ss:.{decimals}f}"'

# Function to round off Matrix elements
from sympy import Number
def round_mat(expr, num_digits):
    return expr.xreplace({n: round(n, num_digits) for n in expr.atoms(Number)})

# Function to round to specified significant figures
from math import floor, log10
def roundsf(value, n):
    if value == 0:
        return 0
    # Calculate the order of magnitude
    magnitude = int(floor(log10(abs(value)))) + 1
    # Calculate the rounding factor based on the desired significant figures
    rounding_factor = n - magnitude
    # Round the value using the rounding factor
    rounded_value = round(value, rounding_factor)
    return rounded_value