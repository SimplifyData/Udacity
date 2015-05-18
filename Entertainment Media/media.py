__author__ = 'onthego'

import webbrowser

class Movie():
    """this is a movie script"""

    valid_ratings = ["G", "PG", "PG-13" , "R"]

    def __init__(self,movie_title,movie_story_line,poster_image,trailer_youtube):
        """ This is a movie class"""
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)