__author__ = 'onthego'


import media
import fresh_tomatoes




toy_story = media.Movie("Toy Story",
                        "A story of a boy",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=NePGVezL1pk")
'''
print(toy_story.storyline)
toy_story.show_trailer()
'''
god_father = media.Movie("God Father", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
              "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg",
              "http://www.imdb.com/video/imdb/vi1348706585/imdb/embed?autoplay=false&width=480")

'''
god_father.show_trailer()
'''

the_lord_of_the_rings = media.Movie("The Lord of the Rings: The Return of the King",
                                    "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
                                    "http://ia.media-imdb.com/images/M/MV5BMjE4MjA1NTAyMV5BMl5BanBnXkFtZTcwNzM1NDQyMQ@@._V1_SX214_AL_.jpg",
                                    "http://www.imdb.com/video/imdb/vi2073101337/imdb/embed?autoplay=false&width=480")

the_lion_king = media.Movie("The Lion King",
                            "Tricked into thinking that he caused the death of his father, a lion cub flees and abandons his destiny as the future king.",
                            "http://ia.media-imdb.com/images/M/MV5BMjEyMzgwNTUzMl5BMl5BanBnXkFtZTcwNTMxMzM3Ng@@._V1_SY317_CR15,0,214,317_AL_.jpg",
                            "http://www.imdb.com/video/imdb/vi3764362265/imdb/embed?autoplay=false&width=480")

movies = [toy_story,god_father,the_lord_of_the_rings,the_lion_king]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.valid_ratings)
print(media.Movie.__doc__)