import fresh_tomatoes
from media import Movie


toy_story = Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://youtu.be/KYz2wyBy3kc")

avatar = Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "https://youtu.be/5PSNL1qE6VY")

sandlot = Movie("The Sandlot", "When Scottie Smalls (Thomas Guiry) moves to a new neighborhood, he manages to make friends with a group of kids who play baseball at the sandlot.", "https://upload.wikimedia.org/wikipedia/en/d/d4/Sandlot_poster.jpg", "https://youtu.be/ec9W8JbFykw")

#sandlot.web_trailer()

sor = Movie("School of Rock", "Overly enthusiastic guitarist Dewey Finn (Jack Black) gets thrown out of his bar band and finds himself in desperate need of work. Posing as a substitute music teacher at an elite private elementary school, he exposes his students to the hard rock gods he idolizes and emulates", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://youtu.be/XCwy6lW5Ixc")

hunger = Movie("The Hunger Games", "When Scottie Smalls (Thomas Guiry) moves to a new neighborhood, he manages to make friends with a group of kids who play baseball at the sandlot.", "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg", "https://youtu.be/FovFG3N_RSU")

inc = Movie("Inception", "Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someone's mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobb's every move.", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://youtu.be/8hP9D6kZseM")

movies = [toy_story, sandlot, avatar, sor, hunger, inc]
fresh_tomatoes.open_movies_page(movies)
