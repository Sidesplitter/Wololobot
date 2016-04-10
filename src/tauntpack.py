from src.taunt import Taunt

class TauntPack:

    name = ""
    description = ""
    taunts = []

    def __init__(self, name: str, description: str):

        if(name == ""):
            raise Exception("Name may not be empty")

        if(description == ""):
            raise Exception("Description may not be empty")

        self.name = name
        self.description = description
        self.taunts = []


    def findMatch(self, message: str) -> Taunt:

        """

        :param message: The message to check
        :return: None if no Taunt was found, otherwise the taunt
        """
        for taunt in self.taunts:

            if(taunt.matches(message)):
                return taunt

        return None