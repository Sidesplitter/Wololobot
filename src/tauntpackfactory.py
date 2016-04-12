import os, logging, sys, yaml

from src.tauntpack import TauntPack
from src.taunt import Taunt

log = logging.getLogger(__name__)

class TauntPackFactory:

    def create(self, path: str) -> TauntPack:
        """
        Create a new tauntpack
        :param path: The directory containing all the taunts and the config.yml
        :return: The tauntpack with all the taunts
        """

        if (path == ""):
            raise Exception("Path may not be empty")

        if (os.path.isfile(path + "/config.yml") == False):
            raise Exception("Directory {dir} does not contain a config.yml".format(dir=path))

        file = open(path + "/config.yml")
        config = yaml.safe_load(file)
        file.close()

        #Create the Tauntpack
        tauntPack = TauntPack(
            config["general"]["name"],
            config["general"]["description"]
        )

        for tauntElem in config["taunts"]:

            try:
                taunt = Taunt(
                    tauntElem["name"],
                    tauntElem["regex"],
                    path + "/" + tauntElem["path"]
                )

                tauntPack.taunts.append(taunt)

            except Exception as e:

                log.error(
                    "Error while adding taunt {taunt}".format(taunt = tauntElem["name"], exec_info = True)
                )

        return tauntPack