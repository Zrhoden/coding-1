# 1
print('A function is a block of code that runs only when called.')
# 2
print ('A parameter is the variable listend inside the parntheses while an argument is the vaule sent to the function when its called')
# 3
print('An if/else conditonal statement is something used to filter and create outcomes based on data')
# 4
print('An integer data is  is a whole number, positive or negative, without decimals, of unlimited length.')
# 5
print('A boolean data type is used to tell you if something is true or false')
#6
print('A comparison operator')
#7
print('An assignment operator')
#8
def checkPasswordLength( length, password):
    if length (password) > 10:
        return('your password is too long')
    elif length (password) < 4:
        return('your password is too short')
    else:
        return('your password was created successfully')
#9
def federalIncomeTax(earnings):
    if earnings == '0 - 12,000':
        return ('you will be taxed 10% plus an additional 3% for the state')
    elif earnings == '12,001 - 50,000':
        return(' you will be taxed 12% plus an additonal 3% for the state')
    elif earnings == '50,001 - 103,000':
        return('you will be taxed 22% plus an addtional 3% for the state')
    elif earnings == '103,001 - 198,000':
        return ('you will be taxed 23% plus an addtional 3% for the state')
    else :
        return('error')
#10 
    
