#tempconv.py
"""Conversion functions between fahrenheit and centigrade"""

#functions
def to_C(x):
    """Returns x converted to centigrade"""
    return 5*(x-32)/9

def to_F(x):
    """Returns x converted to fahrenheit"""
    return 9*x/5.0+32

#constant
freezing_C=0
freezing_F=32

print(to_C(freezing_F))
print(to_F(freezing_C))
