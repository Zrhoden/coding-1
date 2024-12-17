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


def calculateDiscount(membership, name, price):
    # Define the discount rates for each membership
    if membership == "superShopper":
        discount = 0.10
    elif membership == "megaShopper":
        discount = 0.15
    elif membership == "ultraShopper":
        discount = 0.20
    else:
        return "Invalid membership type."
   

    savings = price * discount
    final = price - savings


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      