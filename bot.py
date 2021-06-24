from chai_py import ChaiBot, Update
import datetime 

class AnyBot(ChaiBot):
    def setup(self):
        self.logger.info("Hi there!")
        name = input('Enter the name of your bot:')
        human = input('Who is this human?:')
        self.name = name
        self.human = human

    async def on_message(self, update: Update) -> str:
         return f"Echo: {update.latest_message.text}"

    #def ask_for_number(self):


from chai_py import TRoom

t_room = TRoom([AnyBot()])
t_room.chat()



# """ from chai_py import ChaiBot, Update, TRoom
# import datetime, asyncio
# import nest_asyncio
# nest_asyncio.apply()

# # Important Note: Don't worry about all the asyncio thing as they are just tweaks to allow such bot to be run on Colab. You won't need them if you run your bot locally.

# from chai_py import ChaiBot, Update, TRoom

# class EchoBot(ChaiBot):
#     def setup(self):
#         self.logger.info("Hello, world!")

#     async def on_message(self, update: Update) -> str:
#         return f"Echo: {update.latest_message.text}"

# t_room = TRoom([EchoBot()])
# t_room.chat() """

# from chai_py import ChaiBot, Update

# class Bot(ChaiBot):
#     def setup(self):
#         self.logger.info("Hello, world!")

#     async def on_message(self, update: Update) -> str:
#         return "Hi, I'm ExampleBot."

# from chai_py import TRoom

# t_room = TRoom([Bot()])
# t_room.chat()
