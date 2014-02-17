# convert c2f.py
# - A temperature convert function

def convert(celsius):
    fahrenheit = (9.0/5.0) * celsius + 32
    return fahrenheit

print convert(20)
celsius = int(raw_input("Enter temperature in Celcius: "))
print convert(celsius)

# todo: accept type of input, convert
