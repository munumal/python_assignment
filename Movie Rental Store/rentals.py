

# Module for managing movie rentals


from movie_catalog import available_movies
rented_movies = {}

def rent_movie(customer_name, movie):
    """Rent a movie to a customer."""
    if customer_name not in rented_movies:
        rented_movies[customer_name] = []
    rented_movies[customer_name].append(movie)
    if movie in available_movies:
        available_movies.remove(movie)

def return_movie(customer_name, movie):
    """Return a rented movie."""
    if customer_name in rented_movies and movie in rented_movies[customer_name]:
        rented_movies[customer_name].remove(movie)
        available_movies.append(movie)

def display_rented_movies():
    """Display all rented movies."""
    if rented_movies:
        print("Rented Movies:")
        for customer, movies in rented_movies.items():
            print(f"Customer: {customer}")
            for movie in movies:
                print(f"Title: {movie[0]}, \nGenre: {movie[1]}, \nRental Price: ₹ {movie[2]}.00/-")
    else:
        print("No movies rented.")
