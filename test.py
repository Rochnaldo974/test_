#!/usr/bin/python3

fruit = "apple"
quantity = 3   
pie_crust = "empty"
isOvenOn = False
    
def prep_my_fruit(quantity, fruit, pie_crust):
    print("You put", quantity, fruit, "on the trust")
    pie_crust = "filled with delicious apples"
    return (pie_crust)
   
    

pie_crust = prep_my_fruit(3, "apples", "empty")
print("my pie is", pie_crust)