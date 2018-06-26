"""stores details of movies and shows them users' browser"""
import fresh_tomatoes
import media

title = "Escape Plan"
storyline = "Ray Breslin is the world's foremost authority on structural security. After analyzing every high security prison "\
    "and learning a vast array of survival skills so he can design escape-proof prisons, his skills are put to the test. He's framed"\
    "and incarcerated in a master prison he designed himself. He needs to escape and find the person who put him behind bars."
poster_image = "https://upload.wikimedia.org/wikipedia/en/thumb/5/5d/Escapeplanfilmposter.jpg/220px-Escapeplanfilmposter.jpg"
trailer_youtube_link = "https://www.youtube.com/watch?v=CI4EjV_x_PQ"
Escape_plan = media.Movie(title, storyline, poster_image, trailer_youtube_link)

title = "X-Men:Apocalypse"
storyline = "Since the dawn of civilization, he was worshipped as a god. Apocalypse, the first and most powerful mutant from Marvel’s X-Men universe,"\
    "amassed the powers of many other mutants, becoming immortal and invincible. Upon awakening after thousands of years, he is disillusioned with the world"\
    "as he finds it and recruits a team of powerful mutants, including a disheartened Magneto (Michael Fassbender),"\
    "to cleanse mankind and create a new world order, over which he will reign. As the fate of the Earth hangs in the balance, Raven (Jennifer Lawrence)"\
    "with the help of Professor X (James McAvoy) must lead a team of young X-Men to stop their greatest nemesis and save mankind from complete destruction."
poster_image = "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/X-Men_-_Apocalypse.jpg/220px-X-Men_-_Apocalypse.jpg"
trailer_youtube_link = "https://www.youtube.com/watch?v=COvnHv42T-A"
x_men_apocalypse = media.Movie(
    title,
    storyline,
    poster_image,
    trailer_youtube_link)

title = "Kung Fu Panda"
storyline = "Enthusiastic, big and a little clumsy, Po is the biggest fan of kung fu around... which doesn't exactly come in handy while working every day"\
    "in his family's noodle shop. Unexpectedly chosen to fulfill an ancient prophecy, Po's dreams become reality when he joins the world of kung fu and studies"\
    "alongside his idols, the legendary Furious Five—Tigress, Crane, Mantis, Viper and Monkey—under the leadership of their guru, Master Shifu. But before they"\
    "know it, the vengeful and treacherous snow leopard Tai Lung is headed their way, and it's up to Po to defend everyone from the oncoming threat. Can he turn"\
    "his dreams of becoming a kung fu master into reality? Po puts his heart — and his girth —into the task, and the unlikely hero ultimately finds that his greatest"\
    "weaknesses turn out to be his greatest strengths."
poster_image = "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220px-Kungfupanda.jpg"
trailer_youtube_link = "https://www.youtube.com/watch?v=PXi3Mv6KMzY"
kung_fu_panda = media.Movie(
    title,
    storyline,
    poster_image,
    trailer_youtube_link)

title = "The Intern"
storyline = "In “The Intern,” De Niro stars as Ben Whittaker, a 70-year-old widower who has discovered that retirement isn’t all it’s cracked up to be."\
    "Seizing an opportunity to get back in the game, he becomes a senior intern at an online fashion site, founded and run by Jules Ostin (Hathaway)."
poster_image = "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg"
trailer_youtube_link = "https://www.youtube.com/watch?v=ZU3Xban0Y6A"
the_intern = media.Movie(title, storyline, poster_image, trailer_youtube_link)

title = "The Martian"
storyline = ""
poster_image = "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg"
trailer_youtube_link = "https://www.youtube.com/watch?v=ej3ioOneTy8"
the_martian = media.Movie(title, storyline, poster_image, trailer_youtube_link)

title = "The Shawshank Redemption"
storyline = ""
poster_image = "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg"
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
