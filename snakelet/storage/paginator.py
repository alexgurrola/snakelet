class Paginator:
    def __init__(self, *args, **kwargs):
        # database
        self.collection = args[0]
        self.objectify = self.collection.objectify
        self.collection = self.collection.collection

        # parameters
        self.current = 0 if 'start' not in kwargs else kwargs['start']
        self.find = None if 'find' not in kwargs else kwargs['find']
        self.offset = 0 if 'offset' not in kwargs else kwargs['offset']
        self.sort = None if 'sort' not in kwargs else kwargs['sort']
        self.size = 30 if 'size' not in kwargs else kwargs['size']

    def __iter__(self):
        return self

    def __next__(self):
        limit = self.collection.count() - self.offset
        pages = limit // self.size
        if self.current > pages:
            raise StopIteration
        else:
            # build query
            page = self.collection
            page = page.find() if not self.find else page.find(self.find)
            if self.sort:
                key, value = self.sort
                page = page.sort(key, value)
            page = page.limit(self.size)
            if self.current > 0:
                page = page.skip(self.offset + (self.current * self.size))
            elif self.offset > 0:
                page = page.skip(self.offset)

            # objectify
            documents = []
            for document in page:
                documents.append(self.objectify(document))

            # finalize
            self.current += 1
            return documents


def main():
    pass


if __name__ == '__main__':
    import plac

    try:
        plac.call(main)
    except KeyboardInterrupt:
        print('\nGoodbye!')
