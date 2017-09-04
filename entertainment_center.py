import media
import fresh_tomatoes
#9 Movie class instances
arrival = media.Movie("Arrival", "American science fiction film, 2016",
                      "https://ksscensorthis.com/wp-content/uploads/2017/04/SUiavMWW5Vo.movieposter_maxres.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

fantastic_beasts = media.Movie("La La Land ", "American musical romantic comedy-drama film, 2016",
                               "https://d3fa68hw0m2vcc.cloudfront.net/cee/177322540.jpeg",
                               "https://www.youtube.com/watch?v=0pdqf4P9MB8")

atonement = media.Movie("Atonement", "British romantic war drama film, 2007",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM0ODc2Mzg1Nl5BMl5BanBnXkFtZTcwMTg4MDU1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=rkVQwwPrr4c")

school_of_rock = media.Movie("School of Rock", "American musical comedy film, 2003",
                             "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "American animated comedy film, 2007",
                          "http://is1.mzstatic.com/image/thumb/Video69/v4/22/50/c3/2250c3e7-6b24-a0df-dd8f-dea7321b3ee4/source/1200x630bb.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

cinderella = media.Movie("Cinderella", "American fantasy film, 2015",
                         "http://www.wrightlibrary.org/files/images/Cinderella.jpg",
                         "https://www.youtube.com/watch?v=20DF6U1HcGQ")

alice_in_wonderland = media.Movie("Alice in Wonerland", "American fantasy adventure film, 2010",
                                  "https://vignette1.wikia.nocookie.net/disney/images/7/7e/Alice_In_Wonderland_%282010%29_cover.jpg/revision/latest?cb=20120519233959",
                                  "https://www.youtube.com/watch?v=9POCgSRVvf0")

edward_scissorhands = media.Movie("Edward Scissorhands", "American romantic dark fantasy film, 1990",
                                  "https://i.ytimg.com/vi/bZr28SlINxY/movieposter.jpg",
                                  "https://www.youtube.com/watch?v=M94yyfWy-KI")

dark_shadows = media.Movie("Dark Shadows", "American horror comedy film, 2012",
                           "https://www.warnerbros.com/sites/default/files/styles/key_art_270x400/public/dark_shadows_keyart.jpg?itok=QRANW2wk",
                           "https://www.youtube.com/watch?v=wpWvkFlyl4M")
#list with the movies
movies = [arrival, fantastic_beasts, atonement, school_of_rock, ratatouille, cinderella, alice_in_wonderland, edward_scissorhands, dark_shadows]
#creates HTML page with movies from the list
fresh_tomatoes.open_movies_page(movies)
