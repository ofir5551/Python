class Movie:
    def __init__(self, name, length):
        self.name = name
        self.length = length

class Cinema_Room:
    def __init__(self, movie):
        self.movie = movie

    def AssignMovie(self, movie):
        self.__init__(movie)

    seats = [[True, True, True, True, True, True, True, True, True],
             [True, True, True, True, True, True, True, True, True],
             [True, True, True, True, True, True, True, True, True],
             [True, True, True, True, True, True, True, True, True],
             [True, True, True, True, True, True, True, True, True],
             [True, True, True, True, True, True, True, True, True],
             [True, True, True, True, True, True, True, True, True],
             [True, True, True, True, True, True, True, True, True],
             [True, True, True, True, True, True, True, True, True],
             [True, True, True, True, True, True, True, True, True]]

class Cinema:
    halls = []
    index = 0

    @classmethod
    def orderMovie(number, movieName):
        for i in range(0, 6):
            if halls[i].movie.name == movieName:
                for x in range(0, number):
                    halls[i].seats[index] = False
                    index += 1


m1 = Movie("Avatar", 120)
m2 = Movie("Alice in Wonderland", 90)

Cinema.halls[0].AssignMovie("Avatar")