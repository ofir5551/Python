class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_info(self):
        return str(self.day) + " / " + str(self.month) + " / " + str(self.year)
