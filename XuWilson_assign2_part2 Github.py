
#Wilson Xu, 2/6/23
# Converts temp in Fahrenheit to Celsius, Kelvin, Rankine, Delisle, and Newton

# Get the temp in Fahrenheit from user input
temp_f = float(input("Enter a temperature in degrees Fahrenheit: "))

# Convert the temp to Celsius
temp_c = (temp_f - 32) * 5/9

# Convert the temp to Kelvin
temp_k = temp_c + 273.15

# Convert the temp to Rankine
temp_r = temp_f + 459.67

# Convert the temp to Delisle
temp_de = (100 - temp_c) * 3/2

# Convert the temp to Newton
temp_n = temp_c * 33/100

# Format the converted temp to two decimal places
temp_c = format(temp_c, ".2f")
temp_k = format(temp_k, ".2f")
temp_r = format(temp_r, ".2f")
temp_de = format(temp_de, ".2f")
temp_n = format(temp_n, ".2f")

# Print results
print("\n{:,.2f} degrees Fahrenheit...".format(temp_f),"\n")
print("... in degrees Celsius {:>20} C".format(temp_c))
print("... in degrees Kelvin {:>21} K".format(temp_k))
print("... in degrees Rankine {:>20} R".format(temp_r))
print("... in degrees Delisle {:>20} De".format(temp_de))
print("... in degrees Newton {:>21} N".format(temp_n))

