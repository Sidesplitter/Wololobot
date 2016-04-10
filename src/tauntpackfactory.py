import os, logging, sys

from src.tauntpack import TauntPack
from src.taunt import Taunt

class TauntPackFactory:

    def create(self, path: str) -> TauntPack:

        if (path == ""):
            raise Exception("Path may not be empty")

        if (os.path.isfile(path) == False):
            raise Exception("Directory does not contain a config.ini")

        #Read configuration
        import configparser
        config = configparser.ConfigParser()
        config.read(path)

        #Create the Tauntpack
        tauntPack = TauntPack(
            config["General"]["Name"],
            config["General"]["Description"]
        )

        for key in config["Taunts"]:

            try:
                #Split the config
                regex, path = config["Taunts"][key].split(",")


                taunt = Taunt(
                    key,
                    regex,
                    path
                )

                tauntPack.taunts.append(taunt)

            except:

                e = sys.exc_info()[0]
                logging.error(
                    "Error while adding taunt {taunt}: {error}".format(taunt = key, error =e )
                )

        return tauntPack