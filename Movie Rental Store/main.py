# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:39:45 2024

@author: Musaddique
"""

# Main module to use the movie rental system

from movie_catalog import add_movie, display_available_movies
from rentals import rent_movie, return_movie, display_rented_movies
from earnings import calculate_rental_earnings

# Adding some movies to the catalog
add_movie("Inception", "Sci-Fi", 399)
add_movie("The Godfather", "Crime", 499)
add_movie("Toy Story", "Animation", 299)
add_movie("Grand Turismo", "racing", 399)
add_movie("3 idiots", "Dramedy", 299)
add_movie("Shadow of Tomb Raider", "Adventure", 299)
add_movie("Shutter Island", "Psychological Thriller", 399)



# Renting movies to customers
rent_movie("Adi", ("Grand Turismo", "racing", 399))
rent_movie("Musa", ("The Godfather", "Crime", 499))
rent_movie("Gaudel",("3 idiots","Dramedy",299))



return_movie("Praks", ("Terminator", "Sci-Fi", 399))


display_available_movies()
print("\n \n")
display_rented_movies()





print("\n \n")
earnings = calculate_rental_earnings()
print(f"Total Rental Earnings: ₹ {earnings:.2f}")
