class Query:
    # TODO: Build a structure that extends the current cursor and allows for objectification

    # constructor
    def __init__(self, query):
        self.query = query

    # destructor
    def __del__(self):
        pass

    # types
    def __bool__(self):
        pass

    def __bytes__(self):
        pass

    def __str__(self):
        pass

    # conversions
    def __format__(self, format_spec):
        pass

    def __repr__(self):
        pass

    # comparisons
    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    # iterations
    def __len__(self):
        pass

    def __contains__(self, item):
        pass

    def __next__(self):
        pass

    def __reversed__(self):
        pass

    # chain wrappers
    def count(self):
        pass

    def limit(self):
        pass

    def sort(self):
        pass
