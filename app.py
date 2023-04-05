# Auto-park

# DB ->
#       named as auto =>
#                       [ scheme of auto :
#                           {
#                              "label" : ... ,
#                              "price" : ... ,
#                              "wheels" : ... ,
#                              "color" : ... ,
#                              "number" : "random value"
#                           }
#                        ]

# Amount of auto > 10

# color : red , green , black , yellow , blue

# label : more than 5

# price : from 2000 till 200 000

# number and number length > 12

# Form category dictionary :
# dynamic

# cheap (2000 - 20000) , expensive(100000 - 200000) , medium - (20000 - 100000) - class car
# def sort_car_by_price (arr)
# return {
#   cheap : [],
#   medium : [],
#   expensive : []
# }


# print( cars that we have : for poor , rich , and medium-lvl persons )
# input -> sort : color -> choose on of : blue , green , ... ;  price , label


# for , while

from function.is_exit import is_exit
from function.wheels import wheels
from function.create_autopark import create_autopark
from function.show_autopark import show_autopark
from function.sort_car_by_color import sort_car_by_color
from function.sort_car_by_price import sort_car_by_price

is_running = True
named_as_auto = []
import random

while is_running :
    user_choose = input("""
        a) Creation autopark 
        b) Show autopark
        c) Sort by color
        d) Sort by price
        q) Quit
    
    Answer : """).lower()

    if user_choose == "a":
    
        label_auto = input("Enter label of auto: ")
        price_auto = input("Enter price of auto: ")
        wheels_auto = wheels() 
        color_auto = input("Enter auto color: ")
        autopark=create_autopark (label_auto, price_auto, wheels_auto, color_auto, number_auto=random.randint(1000000000000, 10000000000000))
        if color_auto == 'green' or color_auto == 'red' or color_auto == 'black' or color_auto == 'blue' or color_auto == 'yellow':
            named_as_auto.append(autopark)
            print(named_as_auto)
        else:
            print("Error! Color must be black or blue or red or green or yellow")
        
            
    elif user_choose == "b":
        show_autopark(named_as_auto)
   
    elif user_choose == "c":
        sort_car_by_color(named_as_auto)
    
    elif user_choose == "d":
        for key ,values in sort_car_by_price(named_as_auto).items():
            print(key) 
            for car in values: 
                print(car)     
                
    elif user_choose == "q":
        result = is_exit()
        if result == "y" :
            is_running = False


