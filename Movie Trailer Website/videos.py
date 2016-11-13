import webbrowser

"""A movie class to create instances of movie objects that
can be rendered on to the browser window."""
class Movie():
    def __init__(self,title, story, poster_image, trailer,rating):
        self.title = title
        self.story = story
        self.poster_image = poster_image
        self.trailer = trailer
        self.rating = rating

#A method to show trailer of a movie.
    def show_trailer(self):
        webbrowser.open(self.trailer)