import re, os.path

class Taunt:

    name = ""
    """
    The name of the taunt
    :type str
    """

    regex = ""
    """
    The regex to match in the message
    :type str
    """

    path = ""
    """
    The path of the audio file
    :type str
    """

    def __init__(self, name: str, regex: str, path: str):

        """

        :param name:  The name of the taunt
        :param regex: The regex of the taunt
        :param path: The path to the audio file
        """

        if(name == ""):
            raise Exception("Name may not be empty")

        if(regex == ""):
            raise Exception("Regex may not be empty")

        try:
            re.compile(regex)
        except re.error:
            raise Exception("Regex string is invalid")

        if(os.path.isfile(path) == False):
            raise Exception("Soundfile {file} does not exist".format(file = path))

        self.name = name
        self.regex = regex
        self.path = path

    def matches(self, message: str) -> bool:

        """
        :param message: The message to check
        :return: True if the taunt is matched in the message, false if not
        """
        return re.match(self.regex, message) != None