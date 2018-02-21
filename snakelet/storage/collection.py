from .paginator import Paginator
from ..utilities.conversion import snake


class Collection:
    def __init__(self, manager, document):
        self.manager = manager
        self.document = document
        self.collection_name = snake(self.document.__name__)
        self.collection = self.manager.db[self.collection_name]

    def find(self, search):
        return self.manager.find(self.collection_name, search)

    def find_one(self, search):
        return self.manager.find_one(self.collection_name, search)

    def save(self, document):
        if '_id' not in document:
            self.collection.insert(document)
        else:
            self.collection.update({"_id": document['_id']}, document)

    def refresh(self, document):
        if '_id' in document:
            document.update(self.collection.find_one(document['_id']))

    def remove(self, document):
        if '_id' in document:
            self.collection.remove({"_id": document['_id']})
            document.clear()

    def paginate(self, **kwargs):
        return Paginator(self, **kwargs)

    def objectify(self, document):
        return self.manager.objectify(self.collection_name, document)


def main():
    pass


if __name__ == '__main__':
    import plac

    try:
        plac.call(main)
    except KeyboardInterrupt:
        print('\nGoodbye!')
