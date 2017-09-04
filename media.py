import webbrowser
class Movie():
    """This class provides a way to store movie related information such as its title, description, poster url and youtube trailer url. 
    The function show_trailer(self) allows to watch the trailer"""
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ Constructor for class Movie objects.

        :param movie_title: movie title
        :param movie_storyline: movie storyline
        :param poster_image: poster image url
        :param trailer_youtube: url link to youtube trailer
        :type movie_title: str
        :type movie_storyline: str
        :type poster_image: str
        :type trailer_youtube: str
        :return: object of class Movie with specified params
        :rtype: objects of class Movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """Opens a window with the trailer video"""
        webbrowser.open(self.trailer_youtube_url)
