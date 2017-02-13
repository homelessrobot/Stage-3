import media
import fresh_tomatoes


#Defining 6 instances of the Movie class
inception = media.Movie("Inception", 
                        "A story about a man that’s assembling a team of people in the black market of the dream world.", 
                        "https://www.movieposter.com/posters/archive/main/101/MPW-50904", 
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

dumb_and_dumber = media.Movie("Dumb and Dumber", 
                              "Two best friends set out on an adventure to return a lost briefcase", 
                              "https://www.movieposter.com/posters/archive/main/88/MPW-44013", 
                              "https://www.youtube.com/watch?v=l13yPhimE3o")

shawshank_redemption = media.Movie("Shawshank Redemption",
                                  "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                  "http://www.impawards.com/1994/posters/shawshank_redemption_ver1.jpg",
                                  "https://www.youtube.com/watch?v=6hB3S9bIaco")

the_godfather = media.Movie("The Godfather",
                           "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
                           "https://s-media-cache-ak0.pinimg.com/736x/40/b4/21/40b421c7cfe1b3059d5e50d79e968270.jpg"
                           "https://www.youtube.com/watch?v=sY1S34973zA")

twelve_angry_men = media.Movie("12 Angry Men",
                              "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.",
                              "http://www.impawards.com/1957/posters/twelve_angry_men.jpg",
                              "https://www.youtube.com/watch?v=fSG38tk6TpI")

the_lives_of_the_others = media.Movie("The Lives of the Others",
                                     "In 1984 East Berlin, an agent of the secret police, conducting surveillance on a writer and his lover, finds himself becoming increasingly absorbed by their lives.",
                                     "https://profratigan.files.wordpress.com/2013/07/the-lives-of-others-poster.jpg",
                                     "https://www.youtube.com/watch?v=FppW5ml4vdw")

full_metal_jacket = media.Movie("Full Metal Jacket",
                               "A pragmatic U.S. Marine observes the dehumanizing effects the Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting in Hue.",
                               "http://onset-hollywood.com/wp-content/uploads/2016/04/full-metal-jacket-filming-locations.jpg",
                               "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

#defining the movies list 
movies = [inception, dumb_and_dumber, shawshank_redemption, the_godfather, the_lives_of_the_others, full_metal_jacket]

#opens the movies page file
fresh_tomatoes.open_movies_page(movies)