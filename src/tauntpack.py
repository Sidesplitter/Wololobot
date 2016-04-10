import os

class TauntPack:

    name = ""
    description = ""
    taunts = []
    path = ""

    def __init__(self, name: str, description: str, path: str):

        if(name == ""):
            raise Exception("Name may not be empty")

        if(description == ""):
            raise Exception("Description may not be empty")

        if(path == ""):
            raise Exception("Path may not be empty")

        if(os.path.isdir(path) == False):
            raise Exception("Directory does not exist")

        if(os.path.isfile(path + "/config.ini") == False):
            raise Exception("Directory does not contain a config.ini")

        self.name = name
        self.description = description
        self.path = path


    def findMatch(self, message: str):

        """

        :param message: The message to check
        :return: None if no Taunt was found, otherwise the taunt
        """
        for taunt in self.taunts:

            if(taunt.matches(message)):
                return taunt

        return None