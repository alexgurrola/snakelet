import inspect

from bson.dbref import DBRef
from pymongo import MongoClient

from .collection import Collection
from .document import Document
from ..utilities.conversion import Conversion


class Manager(object):

    def __init__(self, database, host=None, port=None, username=None, password=None, case=None):
        """
        :param database:
        :param host:
        :param port:
        :param username:
        :param password:
        :param case:
        """
        # Configuration
        self.collection_name = Conversion(case)
        self.document_name = Conversion('camel')

        # Driver
        self.client = MongoClient(host=host, port=port)
        self.client[database].authenticate(name=username, password=password)
        self.db = self.client[database]

        # Storage
        self.collections = {}
        self.documents = {}
        self.ref_types = (dict, list, DBRef)

    @staticmethod
    def identify(document):
        """
        Args:
            document:

        Returns:
            str: Name of document
        """
        isclass = inspect.isclass(document)
        if isclass and issubclass(document, Document):
            return document.__name__
        elif not isclass and isinstance(document, Document):
            return type(document).__name__
        else:
            raise TypeError('Value is not an instance or subclass of Document.')

    def collection(self, target):
        """
        Args:
            target:

        Returns:
            Collection:
        """
        if not isinstance(target, str):
            target = self.identify(target)
        if target not in self.collections:
            raise LookupError('Collection ' + target + ' does not exist.')
        return self.collections[target]

    def register(self, *args):
        """
        Args:
            *args: One or more documents

        Returns:

        """
        for document in args:
            if not issubclass(document, Document):
                continue
            identifier = self.identify(document)
            if identifier in self.documents:
                raise LookupError('Document ' + identifier + ' is already registered.')
            self.documents[identifier] = document
            self.collections[identifier] = Collection(self, document)
            self.__setattr__(identifier, Collection(self, document))

    def objectify(self, collection, document):
        """
        Args:
            collection:
            document:

        Returns:
            Document:
        """
        # TODO: This should probably access the correct collection instead
        name = self.document_name.encode(collection)
        if name in self.documents:
            prototype = self.documents[name]()
            if document:
                prototype.update(document)
            # TODO: There needs to be a 'proxy' object that holds the DBRef and hydrates
            # self.hydrate(prototype)
            return prototype
        return document

    def hydrate(self, target):
        """
        Args:
            target:

        Returns:
            object
        """
        if isinstance(target, DBRef):
            # FIXME: This needs to reference the correct collection
            document = self.collection(target.collection).find_one(target.id)
            if document:
                document = self.hydrate(self.objectify(target.collection, document))
            return document
        elif isinstance(target, dict):
            for key, value in target.items():
                if isinstance(value, self.ref_types):
                    target[key] = self.hydrate(value)
        elif isinstance(target, list):
            for i, value in enumerate(target):
                if isinstance(value, self.ref_types):
                    target[i] = self.hydrate(value)

        # return target if nothing else occurred
        return target

    def save(self, *args):
        """
        Args:
            *args: One or more documents

        Returns:

        """
        for document in args:
            self.collection(document).save(document)

    def refresh(self, *args):
        """
        Args:
            *args: One or more documents

        Returns:

        """
        for document in args:
            self.collection(document).refresh(document)

    def remove(self, *args):
        """
        Args:
            *args: One or more documents
        """
        for document in args:
            self.collection(document).remove(document)

    def shutdown(self):
        """
        Returns:

        """
        pass
