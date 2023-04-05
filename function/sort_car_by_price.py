def sort_car_by_price(list_of_car):
    
    cheap_car =[]
    medium_car=[]
    expensive_car=[]
    
    for car in list_of_car:
        if int(car['price'])>=2000 and int(car['price'])< 20000:
            cheap_car.append(car)
        elif int(car['price'])>=20000 and int(car['price'])<100000:
            medium_car.append(car)
        elif int(car['price'])>=100000 and int(car['price'])<200000:
            expensive_car.append(car)
    
    return {
        "cheap:": cheap_car,
        "medium:": medium_car,
        "expensive:": expensive_car
    }

