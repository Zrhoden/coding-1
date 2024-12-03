# Discuss the anatomy of a function

# a Function definition tells the computer the instructions on what we want to do

# data - just means data types

# curly brackets = passing in data into the function definition. This is formally called a parameter

#parameter = placeholder
def modifyMyName(name):
   print('Your new modified name is great' + name)       

#when we pass data into a function call it is called an argument
#argument = evidence, facts, real data.
modifyMyName('Ian')


# Lesson on Conditional Statements
# condtional statements use the 'IF' and 'ELSE' keywords to filter and create specific outcomes based on data.

def verifyAge(age):
   if age > 17:
    print('Congrats! you can buy GTA VI')
   else:
        print('Sorry, you need an adult to buy this game.')

verifyAge(19)