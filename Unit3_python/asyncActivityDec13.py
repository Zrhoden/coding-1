# Number 1

def checkNumber(num):
    if num > 0:
        return "this is a positive number"
    elif num < 0:
        return "this is a negative number"
    else:
        return "this is zero "
   

# Number 2

def movieTicketPrice(age):
    if age <= 10:
        return "$5.00"
    elif 16 <= age < 20:
        return "10.00"
    elif age >= 65:
        return "5.00"
    else:
        return "15.00"
   
   

# Number 3


def discountFunction(membership,itemPrice):
    
    if membership == "superShopper":
        print('you are getting 10 percent off')
        discount= itemPrice * .1
        total= itemPrice - discount
        print(total)
    elif membership == "megaShopper":
          print('you are getting 15 percent off')
          discount= itemPrice * .15
          total= itemPrice - discount
          print(total)
    elif membership == "ultraShopper":
          print('you are getting 20 percent off')
          discount= itemPrice * .2
          total= itemPrice - discount
          print(total)
    else:
        print('Error: sorry, that type of membership doesnt exist')
   

discountFunction('superShopper', 150)    


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      