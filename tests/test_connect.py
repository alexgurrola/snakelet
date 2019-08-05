from snakelet.storage import Document, Manager


class Owner(Document):
    pass


class Cat(Document):
    pass


# Read Configuration
# config = configparser.ConfigParser()
# config.read('tests/config.ini')
# config = config['storage']

# Connect to Database
manager = Manager(
    case='camel',
    # database=config['db'],
    database='snakelet_test',
    # host=config['host'],
    host=None,
    # port=config.getint('port'),
    port=None,
    # username=config['user'],
    username='snakelet_test',
    # password=config.get('pass', raw=True)
    password='e880c7f6bb0a4ed4866d9da2b829e8a3e61b69f4'
)


# Register Types
def test_register():
    manager.register(Owner, Cat)
    assert 'Owner' in manager.documents
    assert 'Cat' in manager.documents


def test_create_single():
    # create document
    owner = Owner()
    owner['name'] = 'Schrödinger'
    assert owner.is_new()
    # persist document
    manager.save(owner)
    assert not owner.is_new()


def test_create_batch():
    owner = manager.Owner.find_one({'name': 'Schrödinger'})
    assert owner is not None
    # save count
    # manager.Cat.count()
    # create cats
    test_set = 10
    for x in range(test_set):
        cat = Cat()
        cat['name'] = '{1} {0}'.format(str(x), 'Pyewacket' if x % 2 == 0 else 'Shoshana')
        cat['owner'] = owner
    # assert count is test_set more
    assert True


def test_find():
    # Fetch and/or Create
    # fetched = manager.Test.find_one({'name': 'example'})
    # if not fetched:
    #     print('unable to find document; creating new document...')
    #     created = Test()
    #     created['name'] = 'example'
    #     print('save:', created)
    #     manager.save(created)
    #     print('persistent:', created)
    # elif 'updated' not in fetched or not fetched['updated']:
    #     print('updating:', fetched)
    #     fetched['updated'] = True
    #     manager.save(fetched)
    # else:
    #     print('fetched:', fetched)
    #     print('removing document...')
    #     manager.remove(fetched)
    assert True


def test_page():
    # Settings
    """
    results = manager.Test.find({'name': 1})
    result_count = results.count()
    """
    # result_count = manager.Test.collection.count()
    # print('count:', result_count)
    #
    # if result_count < 10:
    #     filler = []
    #     for x in range(0, 10):
    #         data = Test({'value': x})
    #         filler.append(data)
    #         manager.save(data)
    #
    # for page in manager.Test.paginate(find={'name': 1}):
    #     for test in page:
    #         print(test)

    assert True
