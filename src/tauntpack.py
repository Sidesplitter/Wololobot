from src.taunt import Taunt

class TauntPack:

    name = ""
    """
    The Name of the tauntpack
    :type str
    """

    description = ""
    """
    The description of the tauntpack
    :type str
    """

    taunts = []
    """
    The taunts in this tountpack
    :type List[Taunt]
    """

    def __init__(self, name: str, description: str):
        """

        :param name: The name of the tauntpack
        :param description: The description of the tauntpack
        """

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