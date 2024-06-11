def main():
    return

if __name__ == '__main__':
    main()

def main():
    data = {
        'full_name': 'shanad nhattu',
        'student_id': 10329069,
        'pizza_toppings': ['ONIONS', 'TOMATO', 'CHICKEN'],
        'movies': [
            {'title': 'SPIDER-MAN', 'genre': 'sci-fi'},
            {'title': 'THE FALL GUY', 'genre': 'action'}
        ]
    }

    # Step 3: Add another movie
    data['movies'].append({'title': 'AMERICAN PSYCHO', 'genre': 'drama'})

    # Step 4: Call function to print student name and ID
    print_student_info(data)

    # Step 6: Print pizza toppings before adding new ones
    print_pizza_toppings(data)

    # Step 5: Add more pizza toppings
    add_pizza_toppings(data, ('ONION', 'PEPPERS'))

    # Step 6: Print pizza toppings after adding new ones
    print_pizza_toppings(data)

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(data)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(data['movies'])


def print_student_info(data):
    full_name = data['full_name']
    first_name = full_name.split()[0]
    print(f"My name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {data['student_id']}.")


def add_pizza_toppings(data, toppings):
    data['pizza_toppings'].extend(toppings)
    data['pizza_toppings'] = [topping.lower() for topping in sorted(data['pizza_toppings'])]


def print_pizza_toppings(data):
    print("My favourite pizza toppings are:")
    for topping in data['pizza_toppings']:
        print(f"- {topping}")


def print_movie_genres(data):
    genres = [movie['genre'] for movie in data['movies']]
    print(f"I like to watch {', '.join(genres[:-1])}, and {genres[-1]} movies.")


def print_movie_titles(movies):
    titles = [movie['title'].title() for movie in movies]
    print(f"Some of my favourite movies are {', '.join(titles[:-1])}, and {titles[-1]}!")


if __name__ == '__main__':
    main()
