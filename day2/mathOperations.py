print(1236 + 5894)
print(869 -582)
print(869 *582)
print(869 /582) # division ALWAYS  generate a float data type by default
print(869 // 582) # now an Int using //, It prints only the number b4 the decimal portion
print(4**2) # expoent or power

# order of operation priority  
# PEMDAS = Parenthesis - exponents - Multiplication/Division - Addidtion/Substraction
# PENDASLR = .... LR = left to right

print(4 * 5 + 8 / 2 - 4)

print(4 * (5 + 8) / 2 - 4)

print(4 * 5 + 8 / (2 - 4))

# test

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
# bmi is equal to the person's weight divided by the person's height squared.

bmi = 84 / 1.65 ** 2

print(bmi)  # value is 30.85399449035813

# to round the value to a specific non decimal number, we can converrt to int

print(int(bmi))  # This will only get the number b4 the decimal portion 30. This is called floating

# use round function to round the # to the next higher or lower value

print(round(bmi)) # will be rounded to the next higher # 31

print(round(bmi, 2)) # to get the next 2 digit after the decimal 30.85





