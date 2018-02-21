import configparser

from bson.dbref import DBRef
from pymongo import MongoClient

from .collection import Collection
from ..utilities.conversion import camel


class Manager(dict):
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    config = configparser.ConfigParser()
    config.read('config.ini')
    config = config['storage']
    client = MongoClient(config['host'], config.getint('port'))
    client[config['db']].authenticate(config['user'], config.get('pass', raw=True))
    db = client[config['db']]
    documents = {}
    ref_types = (dict, list, DBRef)

    def register(self, document):
        identifier = document.__name__
        if identifier not in self.documents:
            self.documents[identifier] = document
            self[identifier] = Collection(self, document)
            return True
        return False

    def objectify(self, collection, document):
        name = camel(collection)
        if name in self.documents:
            prototype = self.documents[name]()
            if document:
                prototype.update(document)
            # TODO: There needs to be a 'proxy' object that holds the DBRef and hydrates
            # self.hydrate(prototype)
            return prototype
        return document

    def hydrate(self, target):
        if isinstance(target, DBRef):
            document = self.find_one(target.collection, target.id)
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

    def find(self, collection, search):
        documents = []
        for document in self.db[collection].find(search):
            documents.append(self.objectify(collection, document))
        return documents

    def find_one(self, collection, search):
        return self.objectify(collection, self.db[collection].find_one(search))

    def shutdown(self):
        pass


def main():
    pass


if __name__ == '__main__':
    import plac

    try:
        plac.call(main)
    except KeyboardInterrupt:
        print('\nGoodbye!')
