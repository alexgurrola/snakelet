from .document import Document
from .paginator import Paginator


class Collection:
    def __init__(self, manager=None, document: Document = None):
        """
        :param manager:
        :param document:
        """
        self.manager = manager
        self.document = document
        self.collection_name = manager.collection_name.encode(self.document.__name__)
        self.collection = self.manager.db[self.collection_name]

    def find(self, search):
        """
        :param search:
        :return:
        """
        # TODO: This should access the internal collection instead
        return self.manager.find(self.collection_name, search)

    def find_one(self, search):
        """
        :param search:
        :return:
        """
        # TODO: This should access the internal collection instead
        return self.manager.find_one(self.collection_name, search)

    def save(self, document: Document):
        """
        :param document:
        :return:
        """
        if '_id' not in document:
            self.collection.insert(document)
        else:
            self.collection.update({"_id": document['_id']}, document, {'upsert': True})

    def refresh(self, document: Document):
        """
        :param document:
        :return:
        """
        if '_id' in document:
            document.update(self.collection.find_one(document['_id']))

    def remove(self, document: Document):
        """
        :param document:
        :return:
        """
        if '_id' in document:
            self.collection.remove({"_id": document['_id']})
            document.clear()

    def paginate(self, find=None, offset=0, size=30, sort=None, start=0):
        """
        :param find:
        :param offset:
        :param size:
        :param sort:
        :param start:
        :return:
        """
        return Paginator(self, find, offset, size, sort, start)

    def objectify(self, document: Document):
        """
        :param document:
        :return:
        """
        # TODO: This should access the internal collection instead
        return self.manager.objectify(self.collection_name, document)
