# Create a function that will determine what
# level of education a college student is in
# based on the number of years they've been in
# school.

# 1 freshman, 2 sophmore, ect...
# 5> masters degree, doctorate degree, ect...

def gradeToTitle():
    year = int(input('what year are you in?'))
    if year == '0':
        print(collegeTitles[0]) 
    elif year == '1':
        print(collegeTitles[1])
    elif year == '2':
        print(collegeTitles[2])
    elif year == '3':
        print(collegeTitles[3])
    elif year == '4':
        print(collegeTitles[4])
    elif year == '5' or year == '6':
            print('you are in a masters program and in grad school')
    elif year =='7'and year <= '10':
            print('you are in a doctorates program and in grad school')
    elif year > '11':
         print('Yo go get a job bro, you been in school TOOOO long bruh smh.')
    else:
        print('Error something went wrong, please check your input')

titleBySchoolYear = (1)

# A list is a data type for collecting
# and organizing other data types.

# we create a list by giving it a varible name and using
# the square brackets to place the data inside of.

listB =[10, 102, 4904]

listofData = ['words and characters', 
              10, 
              10.2324, 
              True, 
              False, 
              listB
              ]
# print(listofData)

collegeTitles= ['You dont have a college title yet, freshman, sophmore, junior, senior']
# print(collegeTitles[0])