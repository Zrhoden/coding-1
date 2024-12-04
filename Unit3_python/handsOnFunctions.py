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


def hoursToMinutes(hour):
   print('minutes: 60')
   print(hour * 60)


hoursToMinutes(10)

# Conditional Statements
# If /else keywords: gives us the ability to control outcomes and make decisions on data.
# food expiration software is an example of using conditonal statements. If the food expires it needs to be thrown away, otherwise, or else it can be eaten.
def foodExpiration(month, date, year):
    expirationMonth = 12
    expirationDate = 5
    expirationYear = 2026
    if date > expirationDate and year > expirationYear:
       print('throw food away')
    else:
       print('food is still good')

foodExpiration(12, 8, 2024)