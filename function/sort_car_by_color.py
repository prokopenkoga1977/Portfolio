def sort_car_by_color(list_of_car):
     for car in list_of_car:
        print("\n")
        print("|====================" + car['color'] + "=====================|\n")
        for key, value  in car.items() :
            if key == "label":
                print(key + " ====> " + str(value))

