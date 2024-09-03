# to conver a data to a different type, we use type-casting/type-conversion
#string to integer
print("123" + "456")  # string

print(int("123") + int("456")) # conversion

#NB: we can convert all data to another type. e.g you cant convert "abc" to an int

# task
# Print the number of letter the user name has
user_name = input(" Enter yout name ")
user_name_length = len(user_name)
print("The number of letters in your name are " + str(user_name_length))