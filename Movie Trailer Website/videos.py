import webbrowser

class Movie():
    def __init__(self,title, story, poster_image, trailer):
        self.title = title
        self.story = story
        self.poster_image = poster_image
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)