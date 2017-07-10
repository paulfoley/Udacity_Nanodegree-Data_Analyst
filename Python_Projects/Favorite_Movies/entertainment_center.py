import media
import fresh_tomatoes

# My Favorite Movies
moana = media.Movie('Moana', "A story of a girl that is out to save her village", 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4MzU5NTExNF5BMl5BanBnXkFtZTgwNzY1MTEwMDI@._V1_UY1200_CR90,0,630,1200_AL_.jpg', 'https://www.youtube.com/watch?v=LKFuXETZUsI')  # noqa
avengers = media.Movie('Avengers', "A story of Super Heros uniting to save the world", 'https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg', 'https://www.youtube.com/watch?v=eOrNdBpGMv8')  # noqa
gladiator = media.Movie('Gladiator', 'A story of a gladiator out of revenge', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTgwMzQzNTQ1Ml5BMl5BanBnXkFtZTgwMDY2NTYxMTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg', 'https://www.youtube.com/watch?v=owK1qxDselE')  # noqa
dragon = media.Movie('How to Train Your Dragon', 'Vikings and dragons learn to co-exist!', 'https://images-na.ssl-images-amazon.com/images/I/91DnBoRk-WL._SL1500_.jpg', 'https://www.youtube.com/watch?v=oKiYuIsPxYk')  # noqa
panda = media.Movie('Kung Fu Panda', 'A panda discovers the power within an saves the world', 'http://chevaliertheatre.com/wp-content/uploads/kung.jpg', 'https://www.youtube.com/watch?v=PXi3Mv6KMzY')  # noqa
star_wars = media.Movie('Star Wars', 'A story of Jedi taking down the empire', 'https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg', 'https://www.youtube.com/watch?v=5UfA_aKBGMc')  # noqa

movies = [moana, avengers, gladiator, dragon, panda, star_wars]

# Use Fresh Tomatoes program to display movies
fresh_tomatoes.open_movies_page(movies)
