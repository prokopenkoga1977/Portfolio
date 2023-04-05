import random

def create_autopark (label_auto, price_auto,wheels_auto, color_auto, number_auto=random.randint(1000000000000, 10000000000000)):
    return {
                "label": label_auto,
                "price": price_auto,
                "wheels": wheels_auto,
                "color": color_auto,
                "number": random.randint(1000000000000, 10000000000000)
    } 
