#1 
numberList = [1,23,56,3,56,3,20,200]
length = len(numberList)
index = length - 1
while index >= 0:
    print(numberList[index])
    index -= 1 
#2
def twoFAlogin():
    correctPassword = 'amazon123'
    correctSecondPassword = 12.33

    print ('Weclome to Amazons 2-Factor Login System')

    while True:
        userPassword = input("Enter Your Normal Password:")

        if userPassword == correctPassword:
            try:
                userScondPassword = float(input('Enter your second password (float):'))
            except ValueError:
                print('Invalid input.The second password must be a number.')
                continue
        if userScondPassword == correctSecondPassword:
            print('Congratulations! You can now access your amazon Account.')
            break
        else:
            print('Second password is incorrect. Please try again.')

    else:
        print(' Normal Password Is Incorrect. Please try again.')

twoFAlogin()