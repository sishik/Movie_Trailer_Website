"""stores details of movies and shows them users' browser"""
import fresh_tomatoes
import media

title = "Escape Plan"
storyline = "Ray, an expert in security systems, is framed for a crime"\
"and sent to a high-tech prison.In order to escape from the prison, he"\
"uses all his knowledge and special skills."
poster_image = "https://upload.wikimedia.org/wikipedia/en/thumb/5/5d/Escapeplanfilmposter.jpg/220px-Escapeplanfilmposter.jpg" #NOQA
trailer_youtube_link = "https://www.youtube.com/watch?v=CI4EjV_x_PQ"
Escape_plan = media.Movie(title, storyline, poster_image, trailer_youtube_link)

title = "X-Men:Apocalypse"
storyline = "The all-powerful mutant Apocalypse who is long revered as a "\
"god wants to cause extinction on earth.The X-Men must work together to"\
"demolish his plans."
poster_image = "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/X-Men_-_Apocalypse.jpg/220px-X-Men_-_Apocalypse.jpg"  #NOQA
trailer_youtube_link = "https://www.youtube.com/watch?v=COvnHv42T-A"
x_men_apocalypse = media.Movie(
    title,
    storyline,
    poster_image,
    trailer_youtube_link)

title = "Kung Fu Panda"
storyline = "When an obese Po the Panda, a kung fu enthusiast, gets"\
"selected as the Dragon Warrior, he decides to team up with the Furious"\
"Five and destroy the evil forces that threaten the Valley of Peace."
poster_image = "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220px-Kungfupanda.jpg"   #NOQA
trailer_youtube_link = "https://www.youtube.com/watch?v=PXi3Mv6KMzY"
kung_fu_panda = media.Movie(
    title,
    storyline,
    poster_image,
    trailer_youtube_link)

title = "The Intern"
storyline = "Seventy-year-old Ben Whittaker realises that retirement isn't "\
"an enjoyable experience. As a result, he decides to work as an intern at "\
"an online fashion store managed by an extremely sceptical boss."
poster_image = "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg"   #NOQA
trailer_youtube_link = "https://www.youtube.com/watch?v=ZU3Xban0Y6A"
the_intern = media.Movie(title, storyline, poster_image, trailer_youtube_link)

title = "The Martian"
storyline = "Mark Watney is stranded on the planet of Mars after his crew"\
"leaves him behind, presuming him to be dead due to a storm."\
"With minimum supply, Mark struggles to keep himself alive."
poster_image = "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg"  #NOQA
trailer_youtube_link = "https://www.youtube.com/watch?v=ej3ioOneTy8"
the_martian = media.Movie(title, storyline, poster_image, trailer_youtube_link)

title = "The Shawshank Redemption"
storyline = "Andy Dufresne, a successful banker, is arrested for the murders"\
"of his wife and her lover, and is sentenced to life imprisonment at the"\
"Shawshank prison. He becomes the most unconventional prisoner."
poster_image = "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg" #NOQA
trailer_youtube_link = "https://www.youtube.com/watch?v=6hB3S9bIaco"
shawshank = media.Movie(title, storyline, poster_image, trailer_youtube_link)

# stores the movie names into a list
movies = [
    Escape_plan,
    x_men_apocalypse,
    kung_fu_panda,
    the_intern,
    the_martian,
    shawshank]

# Open the movie website in the user's browser, featuring the movies above.
fresh_tomatoes.open_movies_page(movies)
