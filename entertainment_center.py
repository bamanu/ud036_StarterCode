"""This module will collect all the different Movie instances
and open the fresh tomatoes page showing the list of the movies

This file is made to be executed with no parameters.

"""

import media
import fresh_tomatoes

_TOY_STORY = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

_AVATAR = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


_AMELIE = media.Movie("Amelie",
                     "The story of a girl and the small important things in life",
                     "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
                     "https://www.youtube.com/watch?v=HUECWi5pX7o")


_RATATOUILLE = media.Movie("Ratatouille",
                          "Storyline",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

_MIDNIGHT_IN_PARIS = media.Movie("Midnight in Paris",
                                "Storyline",
                                "http://t3.gstatic.com/images?q=tbn:ANd9GcTk3ssys2bKM5-U6XMgvoD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

_HUNGER_GAMES = media.Movie("The Hunger Games",
                           "Storyline",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

#default_movie = media.Movie("not a film")

_MOVIES = [_TOY_STORY, _AVATAR, _AMELIE, _RATATOUILLE, _MIDNIGHT_IN_PARIS, _HUNGER_GAMES]
fresh_tomatoes.open_movies_page(_MOVIES)

#print (media.Movie.__name__)
#print (media.Movie.__module__)
