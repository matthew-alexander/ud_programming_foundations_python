import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life", 
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


avatar = media.Movie("Avatar", 
                    "A marine on an alien planet", 
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", 
                    "https://www.youtube.com/watch?v=-9ceBgWV8io")



shin_godzilla = media.Movie("Shin Godzilla", 
                            "Monstor shows up and wrecks stuff", 
                            "https://upload.wikimedia.org/wikipedia/en/6/64/Shin_Godzilla_US_poster.jpg", 
                            "https://www.youtube.com/watch?v=zgyq6YKeIms")

knight_of_cups = media.Movie("Knight of Cups", 
                            "Pleasure vs something higher", 
                            "https://upload.wikimedia.org/wikipedia/en/c/c4/Knight_of_Cups_poster.jpg", 
                            "https://www.youtube.com/watch?v=bC-3rnv_b3o")

movies = [toy_story, avatar, shin_godzilla, knight_of_cups]

#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__module__)