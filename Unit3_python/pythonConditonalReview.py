# Functions are just instructions for the computer to know what to do with data
#conditonal statments use the if/else
#keywords to make descions and outcomes
def welcomeMsgByTime(number, time):
    if time == 'am':
       print('good morning')
       print(str(number) + time)
    elif time == 'pm':
        print('Good evening')
        print(str(number) + time)
    else:
        print('sorry, did not understand your input')

def numericalGrade (grade):
    if grade == '96':
        print('A')
    elif grade == '42':
        print('F')
        