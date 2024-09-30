# Module for managing the movie catalog


available_movies = []

def add_movie(title, genre, rental_price):
    movie = (title, genre, rental_price)
    available_movies.append(movie)

def display_available_movies():
    if available_movies:
        print("Available Movies:")
        for movie in available_movies:
            print(f"Title: {movie[0]}, \t\nGenre: {movie[1]}, \nRental Price: ₹ {movie[2]}.00/-")
    else:
        print("No movies available.")


""" --test code--
add_movie("Grand Turismo", "Racing", 130)
display_available_movies()

"""