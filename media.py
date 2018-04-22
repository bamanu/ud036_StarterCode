"""This module content the Movie class definition

"""
import webbrowser

class Movie():
    """
    This class provides a way to store movie related information
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self,
                 movie_title,
                 movie_storyline="No storyline found",
                 poster_image="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg",
                 trailer_youtube="https://www.youtube.com/watch?v=IYnsfV5N2n8"):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Open the trailer of the movie
        This trailer has to be previously set in "trailer_youtube_url"
        """
        webbrowser.open(self.trailer_youtube_url)
