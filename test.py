#!/usr/bin/python3

fruit = "apple"
quantity = 3   
pie_crust = "empty"
isOvenOn = False
    
def prep_my_fruit(quantity, fruit, pie_crust):
    print("You put", quantity, fruit, "on the trust")
    pie_crust = "filled with delicious apples"
    return (pie_crust)

def turn_oven_on(isOvenOn):
    isOvenOn = True
    return (isOvenOn)
   
    

pie_crust = prep_my_fruit(3, "apples", "empty")
print("my pie is", pie_crust)
print("Is the oven turned on ?", turn_oven_on(isOvenOn))
