import webbrowser

class Movie():
    def __init__(self, movie_title, story_line, poster_image_url, trailer_youtube_url):
        '''
        INPUT:initialize with -
            movie_title: The title of your movie as a string
            story_line: The storyline of your movie as a string
            poster_image_url: url link to poster image as a string
            trailer_youtube_url: url link to youtube trailer as a string
        OUTPUT: None
        '''
        self.title = movie_title
        self.storyline = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def web_trailer(self):
        '''
        INPUT: None
        OUTPUT: None
        This method will start the trailer in trailer_youtube_url that lives on the instantiated object of the class Movie
        '''
        webbrowser.open(self.trailer_youtube_url)
