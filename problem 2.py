# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:53:30 2024

@author: Musaddique
"""


inventory = {
    'strawberry': (10, 50),
    'banana': (5, 100),
    'orange': (8, 75)
}


def update_quantity(item, quantity_sold):
    if item in inventory:
        price, available_quantity = inventory[item]
        if quantity_sold <= available_quantity:
            inventory[item] = (price, available_quantity - quantity_sold)
            print(f"Updated {item}: {inventory[item]}")
        else:
            print(f"Error: Not enough {item} in stock.")
    else:
        print(f"Error: {item} does not exist in the inventory.")


update_quantity('apple', 20)
update_quantity('banana', 15)
update_quantity('orange', 5)
