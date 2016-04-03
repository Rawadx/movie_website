import webbrowser

# Creating the constructor of the class Movie
class Movie:
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


# defining the function show_trailer which is declared in the imported webbrowser library        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

