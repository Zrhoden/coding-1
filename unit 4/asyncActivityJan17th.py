#1
campingSupplies= ['tent', 'sleeping bag', 'flashlight', 'camping knife']
campingSupplies.reverse()
print(campingSupplies)
#2
campingSupplies.append('lighter')
print(campingSupplies)
#3
campingFood = ['marshmellows','gram crackers','chocolate','chicken hot dogs','water']

campingStuff = campingSupplies + campingFood
print(campingStuff)
# 4
campingStuff.remove('flashlight')
campingStuff.insert(1, 'camp fire kit')
print(campingStuff)