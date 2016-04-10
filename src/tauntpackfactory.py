import os, logging, sys, yaml

from src.tauntpack import TauntPack
from src.taunt import Taunt

class TauntPackFactory:

    def create(self, path: str) -> TauntPack:

        if (path == ""):
            raise Exception("Path may not be empty")

        if (os.path.isfile(path + "/config.yml") == False):
            raise Exception("Directory does not contain a config.yml")

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

                logging.exception(
                    "Error while adding taunt {taunt}".format(taunt = tauntElem["name"])
                )

        return tauntPack