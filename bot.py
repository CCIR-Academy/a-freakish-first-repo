from chai_py import ChaiBot

class mathbot(ChaiBot):
    def setup(self, date_created, creator, nickname):
        self.logger.info("Hi there!")
        self.date_created = date_created
        self.creator = creator
        self.nickname = nickname

    def print_all_data(self):
        print(self.date_created, self.creator, self.nickname)

bot = mathbot(1, aasu, hell)

