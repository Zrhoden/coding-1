# What are loops
# A python loop is a programming concept where
# code repeats itself under specific conditons.

#In python, there are 2 versions of loops; for loop and
# while loop.

# While Loops - A type of loop that will repeat itself
# so long as some conditon is true.


normalAttack = 2
specialAttack = 4
increaseHealth = 3
def battleFunction():
    hp = 10
    while hp > 0:
         print('do you want to attack?')
         print(hp)
         hp -= normalAttack
         keepGoing = input(' do you want to keep playing?')
         if keepGoing == 'y':
             print('run function again')
         else:
             print('game over')

battleFunction()

# For Loops - this is a type of loop that iterates over a collection
# of data and will run a specific of instructions on data.

# x in this example, is an iterator. This x represents the numbers
#in the list.

#for every number, we want to simply print it out.

numbers = [1, 2, 3, 4, 5 ,6, 7, 8, 9]

for x in numbers:
    print(x)
    attackValues = [10,25,50, 90]

for attacks in attackValues:
    print (attacks * 2)


# Create a function where item over 50.00 get a 10% discount
def shoppingDiscountFunction():
    shoppingCart = []
    customerItem = input ('how much does this item cost?')
    shoppingCart.append(shoppingCart)
    print('here are the item porice in your cart.')
    print(shoppingCart)

shoppingDiscountFunction()