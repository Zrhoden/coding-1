# Loops -  A construct in programming 
# where instructions will repeat over and 
# over until a specfific condtion is met.

# While - is special type of loop where
# instructions will repeat themselves 
# so long as a condition is true
def repeatMsg():
      x = 2
      while x == 2:
         print('this message will repeat forever')

def passwordLoops():
     correctPW = '123abc'
     userPw=input('please enter your password:')
     while userPw != correctPW:
        print('incorrect pw. Try again')
        userPw=input('please enter your password')
     if userPw == correctPW:
         print('congrats')
passwordLoops()

def inventoryLoop():
    userInventory =[]
    pickupItem= input('what item are you tying to pick up?:')
    while len(userInventory) < 4:
        userInventory.append(pickupItem)
        print('these are the items in your bag:')
        print(userInventory)
        pickupItem= input('what item are you picking up?')
# def replaceInventoryItem():
# def removeInventoryItem():

def rngGame():
    randomNumber = random.randrange(1,11)
    userGuess= ''
    while randomNumber != userGuess:
        userGuess = input("Guess a number between 1 and 10")
        print("incorrect guess, try again")





















