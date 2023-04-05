def show_autopark(list_of_car):
    for car in list_of_car:
        print("\n")
        print("|====================" + car['label'] + "=====================|\n")
        for key , value in car.items() :
            if key == "number":
                print(key + " ====> " + str(value))
                continue
            print(key + " ====> " + value)

