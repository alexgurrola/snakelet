import re


def snake(string): return re.sub("([A-Z])", "_\\1", string).lower().lstrip("_")


def camel(string): return "".join(map(str.capitalize, string.split("_")))
