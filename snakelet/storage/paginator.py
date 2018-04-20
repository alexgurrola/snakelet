from .query import Query


class Paginator(Query):
    def __init__(self, collection,
                 find: dict = None,
                 offset: int = 0,
                 size: int = 30,
                 sort: str = None,
                 start: int = 0):
        """
        Args:
            collection:
            find (dict):
            offset (int):
            size (int):
            sort (str):
            start (int):
        """

        super().__init__(None)

        # database
        self.objectify = collection.objectify
        self.collection = collection.collection

        # parameters
        self.current = start
        self.find = find
        self.offset = offset
        self.sort = sort
        self.size = size

    def __iter__(self):
        """
        Returns:

        """
        return self

    def __next__(self):
        """
        Returns:

        """
        # FIXME: This should be a local value with a find to ensure we get an accurate count
        limit = self.collection.count() - self.offset
        pages = limit // self.size
        if self.current > pages:
            raise StopIteration
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
        self.current += 1
        return [self.objectify(document) for document in page]
