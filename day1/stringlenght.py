# Ask user name as a variable and calculate how many characters 

user_name = input("What is your name ")
user_name_length = len(user_name)
print(f"Your name is {user_name} and it is made with {user_name_length} characters.")

# All in one line of code

print(f"Your name is {input('What is your name? ')} and it is made with {len(input('What is your name? '))} characters.") # input twice

#Calling input() twice will ask the question twice. 
# #To avoid this and still achieve the desired result in one line,
# #you need to use a temporary variable within the same line of code. 
# #Here's a solution using a lambda function to achieve it:
print((lambda user_name: f"Your name is {user_name} and it is made with {len(user_name)} characters.")(input("What is your name? "))) # input once


