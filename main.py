import random
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    tomorrows_movie = get_random_movie()

    while tomorrows_movie == movie: # is
        tomorrows_movie = get_random_movie();

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>" # argument {0} and {1}
    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + tomorrows_movie + "</li>"
    content += "</ul>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movie_titles = ["The Incredibles", "Toy Story", "The Robinsons", "Get Smart", "Charlie's Angles"];

    # TODO: randomly choose one of the movies, and return it
    position = random.randrange(0, len(movie_titles) - 1); #randint and choice

    return movie_titles[position]

app.run()