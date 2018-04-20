from .document import Document
from .paginator import Paginator


class Collection:
    def __init__(self, manager, document):
        """
        Args:
            manager:
            document:
        """
        self.manager = manager
        self.document = document
        self.collection_name = self.manager.collection_name.encode(self.document.__name__)
        self.collection = self.manager.db[self.collection_name]

    def find(self, *args, **kwargs):
        """
        Args:
            *args:
            **kwargs:

        Returns:

        """
        # return Query(self.collection.find(*args, **kwargs))
        return [self.objectify(document) for document in self.collection.find(*args, **kwargs)]

    def find_one(self, *args, **kwargs):
        """
        Args:
            *args:
            **kwargs:

        Returns:

        """
        return self.objectify(self.collection.find_one(*args, **kwargs))

    def save(self, *args):
        """
        Args:
            *args: One or more documents
        """
        for document in args:
            if not isinstance(document, Document):
                continue
            if '_id' not in document:
                self.collection.insert(document)
            else:
                self.collection.update({
                    "_id": document['_id']
                }, document, upsert=True)

    def refresh(self, *args):
        """
        Args:
            *args: One or more documents
        """
        for document in args:
            if not isinstance(document, Document) or '_id' not in document:
                continue
            document.update(self.collection.find_one(document['_id']))

    def remove(self, *args):
        """
        Args:
            *args: One or more documents
        """
        for document in args:
            if not isinstance(document, Document) or '_id' not in document:
                continue
            self.collection.remove({"_id": document['_id']})
            document.clear()

    def paginate(self, **kwargs):
        """
        Args:
            **kwargs:

        Returns:
            Paginator:
        """
        return Paginator(self, **kwargs)

    def objectify(self, document):
        """
        Args:
            document:

        Returns:
            Document:
        """
        if not callable(self.document):
            raise LookupError('Unable to associate Document in Collection.')
        prototype = self.document()
        prototype.update(document)
        return prototype
