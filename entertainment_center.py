import media
import fresh_tomatoes
#9 Movie class instances
arrival = media.Movie("Arrival", "Arrival is a 2016 American science fiction film directed by Denis Villeneuve",
                      "https://ksscensorthis.com/wp-content/uploads/2017/04/SUiavMWW5Vo.movieposter_maxres.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

fantastic_beasts = media.Movie("La La Land ", "This original musical about everyday life explores the joy and pain of pursuing your dreams",
                               "https://d3fa68hw0m2vcc.cloudfront.net/cee/177322540.jpeg",
                               "https://www.youtube.com/watch?v=0pdqf4P9MB8")

atonement = media.Movie("Atonement", "Atonement is a 2007 British romantic war drama film",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM0ODc2Mzg1Nl5BMl5BanBnXkFtZTcwMTg4MDU1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=rkVQwwPrr4c")

school_of_rock = media.Movie("School of Rock", "School of Rock is a 2003 musical comedy film",
                             "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "American computer-animated comedy film produced by Pixar and released by Buena Vista Pictures Distribution",
                          "http://is1.mzstatic.com/image/thumb/Video69/v4/22/50/c3/2250c3e7-6b24-a0df-dd8f-dea7321b3ee4/source/1200x630bb.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

cinderella = media.Movie("Cinderella", " The film is based on the eponymous folk tale and inspired in part by Walt Disney's 1950 animated film of the same name",
                         "http://www.wrightlibrary.org/files/images/Cinderella.jpg",
                         "https://www.youtube.com/watch?v=20DF6U1HcGQ")

alice_in_wonderland = media.Movie("Alice in Wonerland", "Story of a girl, who didn't afraid of pursuing her dreams",
                                  "https://vignette1.wikia.nocookie.net/disney/images/7/7e/Alice_In_Wonderland_%282010%29_cover.jpg/revision/latest?cb=20120519233959",
                                  "https://www.youtube.com/watch?v=9POCgSRVvf0")

edward_scissorhands = media.Movie("Edward Scissorhands", "Story of an artificial man named Edward, an unfinished creation who has scissor blades instead of hands",
                                  "https://i.ytimg.com/vi/bZr28SlINxY/movieposter.jpg",
                                  "https://www.youtube.com/watch?v=M94yyfWy-KI")

dark_shadows = media.Movie("Dark Shadows", "An imprisoned vampire, Barnabas Collins, is set free and returns to his ancestral home",
                           "https://www.warnerbros.com/sites/default/files/styles/key_art_270x400/public/dark_shadows_keyart.jpg?itok=QRANW2wk",
                           "https://www.youtube.com/watch?v=wpWvkFlyl4M")
#list with the movies
movies = [arrival, fantastic_beasts, atonement, school_of_rock, ratatouille, cinderella, alice_in_wonderland, edward_scissorhands, dark_shadows]
#creates HTML page with movies from the list
fresh_tomatoes.open_movies_page(movies)
