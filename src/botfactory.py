import os, logging

from src.bot import Bot
from src.tauntpackfactory import TauntPackFactory

log = logging.getLogger(__name__)

class BotFactory:

    def create(self, tauntPath: str):
        """

        :param tauntPath: The folder in which all the tauntpacks are located
        :return Bot:
        """

        if(os.path.isdir(tauntPath) == False):
            raise Exception("Path for taunts does not exist")

        bot = Bot()

        dirs = next(os.walk(tauntPath))[1]

        for i in dirs:

            path = os.path.join(tauntPath, i)

            if(os.path.isfile(path + "/config.yml") == False):
                log.error("{dir} does not have a config.yml, skipping...".
                                                  format(dir=i))
                continue

            try:
                tauntPack = TauntPackFactory().create(path)

                bot.tauntPacks.append(tauntPack)
                log.info("Loaded tauntpack {name}".format(name=tauntPack.name))

            except Exception as e:
                log.error('failed to load tauntpack', exec_info=True)

        return bot