import webbrowser

class Movie():
    def __init__(self, movie_title, story_line, poster_image_url, trailer_youtube_url):
        '''
        INPUT:initialize our class with stuff
        '''
        self.title = movie_title
        self.storyline = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def web_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
