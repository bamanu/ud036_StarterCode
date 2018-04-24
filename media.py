"""This module content the Movie class definition

"""
import webbrowser


class Movie():
    """This class provides a way to store movie related information

        This class was made to populate the fresh_tomatoes web page.
        Every movie will have the basic information of the movie,
        including a poster and a trailer in a video.

    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self,
                 movie_title,
                 movie_storyline="No storyline found",
                 poster_image="https://upload.wikimedia.org/"
                 "wikipedia/commons/a/ac/No_image_available.svg",
                 trailer_youtube="https://www.youtube.com/"
                 "watch?v=IYnsfV5N2n8"):
        """Constructor

        Args:
            movie_title (str): the name of the movie
            movie_storyline (str): the description of the story.
                 By default: "No storyline found",
            poster_image (str): the image of the main poster of the movie.
                 By default: a "no image available" image
            trailer_youtube (str): the trailer of the movie in youtube.
                 It has to be the complete url.
                 By default: ASDF Movie 1

            TODO:make a default video with 20 seconds of "no trailer available"
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Open the trailer of the movie in a web browser.
        This trailer has to be previously set in "trailer_youtube_url"
        """
        webbrowser.open(self.trailer_youtube_url)
