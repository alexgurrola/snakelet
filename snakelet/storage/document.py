class Document(dict):
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    """
    def __init__(self, **kwargs):
        # Parental
        super().__init__(**kwargs)
        self.__meta__ = {}

    def __add_meta__(self, key, type):
        self.__meta__[key] = type
        return
    """
