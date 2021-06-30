from chai_py import ChaiBot, Update
import datetime 

class AnyBot(ChaiBot):
    def setup(self):
        self.logger.info("Hi there!")
        name = input('Enter the name of your bot:')
        human = input('Who is this human?:')
        self.name = name
        self.human = human
        self.time_created = datetime.datetime.now()


    async def on_message(self, update: Update) -> str:
         return f"Echo: {update.latest_message.text}"

    

