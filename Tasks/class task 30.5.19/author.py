import date

class Author():
    def __init__(self, name, birth_date):
        self.name = name
        self.bday = birth_date

    def get_info(self):
        return "The author is: " + self.name + ". Birth date is: " + self.bday.get_info()

