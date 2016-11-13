import videos
import fresh_tomatoes

"""Using the imdb api to get the movie details from imdb website. """
from imdb import IMDb

#create an instance of IMDb() object
ia = IMDb()

#list of movies to display on
complete_movie_list=[] the webpage.

#A key,value dict with movie names and trailer url #pairs
movie_list={"Harry potter and the sorcerer's stone": "https://youtu.be/VyHV0BRtdxo",
            "Vanilla Sky":"https://youtu.be/k09OX40NLUw",
            "Saw":"https://youtu.be/S-1QgOMQ-ls",
            "Doctor strange":"https://youtu.be/Lt-U_t2pUHI",
            "Pink floyd the wall":"https://youtu.be/ZIhW1XIAY9M",
            "Silence of the lambs":"https://youtu.be/LOfH7s__hMY"
            }

"""search movies from the list to get their movieids
Now use the movieids to fetch other fields"""
for the_movie, the_trailer in movie_list.items():
    search_results = ia.search_movie(the_movie)
    movie_id = ia.get_movie(search_results[0].movieID)
    plot = movie_id.get('plot outline')
    poster = movie_id.get('cover url')
    rating = movie_id.get('rating')
    #print movie_id, plot, poster, rating
    a_movie = videos.Movie(movie_id, plot, poster,the_trailer,rating)
    complete_movie_list.append(a_movie)


#Make a call to the fresh_tomatoes file to render the movies on a browser as required.
fresh_tomatoes.open_movies_page(complete_movie_list)