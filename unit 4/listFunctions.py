# lists = a data type for collecting and storing
# other data types into one variable.
# We can store any data type inside of a list including 
# other lists.
# We can store duplicate data inside of lists
# We can locate and access data in a list
# by its index position
# Lists are changeable. We can add and remove things from them.
skii_trip_items= ['snow boots', 'heavy boots']

# append() method - allows us to add utems to a list.
# the new added item will be added to the back of the list.
skii_trip_items.append('gloves')
skii_trip_items.append('thick socks')
print(skii_trip_items)

# insert() method - allows us to add an item to a list, 
# and also dictate what position that item will be at.
# insert takes 2 arguments, the index where where you want to 
# place the data, and the actual data.

skii_trip_items.insert(2, 'googles')
print(skii_trip_items)

# pop() method - allows us to remove the last item in a list
skii_trip_items.pop()
print(skii_trip_items)

# remove() method - allow us to remove an item from the list
# based specifically on the data's value
skii_trip_items.remove('snow boots')
print(skii_trip_items)

# clear() method - allows us to delete the entire list
skii_trip_items.clear()
print(skii_trip_items)

# del function
# del skii_trip_items

def clothingBySeason():
 summerClothes = []
 winterClothes =[]
 clothingSlection= input('what are you wearing?')
 if clothingSlection == 'tee-shirt':
    summerClothes.append('tee-shirt')
    print('here is your summer collection:')
    print(summerClothes)

clothingBySeason()

def favoriteRestaurant():
  restaurants = [' wendys', 'chick-fil-a', 'KFC']
  print(restaurants)
response = input('What is your favorite restaurant?')
print('your favorite restaurant is' + response)