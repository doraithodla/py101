def convert(temp, unit):
    unit = unit.lower()
    if unit == "c":
        temp = 9.0 / 5.0 * temp + 32
        return "%s degrees Fahrenheit" % temp
    if unit == "f":
        temp = (temp - 32) / 9.0 * 5.0
        return "%s degrees Celsius" % temp


temp = int(input("What is the temperature?\n"))
unit = input("Please enter the unit of measure (f or c):\n")

print(convert(temp, unit))
