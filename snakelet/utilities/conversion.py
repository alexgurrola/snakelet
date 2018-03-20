import re


def snake(string: str):
    """
    :param string:
    :return:
    """
    return re.sub("([A-Z])", "_\\1", string).lower().lstrip("_")


def camel(string: str):
    """
    :param string:
    :return:
    """
    return "".join(map(str.capitalize, string.split("_")))


class Conversion:
    cases = {
        'snake': snake,
        'camel': camel
    }

    def __init__(self, case: str = None):
        """
        :param case:
        """
        self.case = self.cases['snake' if not case or case not in self.cases else case]

    def encode(self, data: str):
        """
        :param data:
        :return:
        """
        return self.case(data)
