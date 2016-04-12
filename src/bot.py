import discord, logging
from aiohttp.websocket import Message

log = logging.getLogger(__name__)

class Bot(discord.Client):

    tauntPacks = None
    """
    The loaded tauntpack
    :type list[TauntPack]
    """

    def __init__(self, **options):

        super().__init__(**options)

        self.client = discord.Client()
        self.tauntPacks = []

    async def on_ready(self):
        """
        Gets called when the bot is logged in
        :return:
        """
        log.info("Logged in as {user} with id {id}".format(
            user = self.user.name,
            id = self.user.id
        ))

    async def on_message(self, message=discord.Message):
        """
        Gets called when a message is sent to the bot
        :param message: The message
        :return:
        """
        for tauntPack in self.tauntPacks:

            taunt = tauntPack.findMatch(message.content)

            if(taunt != None):

                log.info("Taunt {name} from {pack} got called by {user}".format(
                    name=taunt.name,
                    pack=tauntPack.name,
                    user=message.author
                ))
                break


