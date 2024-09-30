# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:00:19 2024

@author: Musaddique
"""

# Module for calculating rental earnings


from rentals import rented_movies


def calculate_rental_earnings():
    
    total_earnings = 0
    for movies in rented_movies.values():
        for movie in movies:
            total_earnings += movie[2]
    return total_earnings
