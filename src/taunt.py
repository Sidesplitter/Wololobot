import re, os.path

class Taunt:

    name = ""
    regex = ""
    path = ""

    def __init__(self, name: str, regex: str, path: str):

        if(name == ""):
            raise Exception("Name may not be empty")

        if(regex == ""):
            raise Exception("Regex may not be empty")

        try:
            re.compile(regex)
        except re.error:
            raise Exception("Regex string is invalid")

        if(os.path.isfile(path) == False):
            raise Exception("Soundfile does not exist")

        self.name = name
        self.regex = regex
        self.path = path

    def matches(self, message: str) -> bool:

        """
        :param message: The message to check
        :return: True if the taunt is matched in the message, false if not
        """
        return re.match(self.regex, self.regex) != None