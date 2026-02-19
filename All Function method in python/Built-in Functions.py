num_str = "10"
integer_val = int(num_str) 
print(integer_val)  # Output: 10 converted string to integer

float_val = 5.99
changed_integer = int(float_val)
print(changed_integer)  # Output: 5 converted float to integer (truncated)

#print using f-string
print(f"The integer value is: {integer_val}, and the changed integer value is: {changed_integer}")
#using value together
print(integer_val, changed_integer)

#float convertion examples
num_int = 5
float_num = float(num_int)      # Converts integer 5 to decimal number 5.0
str_float = "3.14"
parsed_float = float(str_float) # Converts string "3.14" to decimal number 3.14

print(f"float(): {float_num},  {parsed_float}")

#complex number conversion
real = 7
imageinary = 9
complex_num = complex(real, imageinary) # Creates a complex number 2 + 3j
print(complex_num)  # Output: (2+3j)
print(f"complex(): {complex_num}")

number = 5
