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
    owner = manager.collection('Owner').find_one({'name': 'Schrödinger'})
    assert owner is not None
    # save count
    initial_count = manager.collection('Cat').collection.count()
    # create
    batch = 20
    # cats = []
    for x in range(batch):
        # create reference
        cat = Cat()
        # cats.append(cat)
        # add data
        cat['name'] = '{1} {0}'.format(str(x), 'Pyewacket' if x % 2 == 0 else 'Shoshana')
        # add reference
        cat['owner'] = owner
        # persist object
        manager.collection('Cat').save(cat)
    # assert count is test_set more
    complete_count = manager.collection('Cat').collection.count()
    assert initial_count == complete_count - batch


def test_page():
    # Settings
    """
    results = manager.Test.find({'name': 1})
    result_count = results.count()
    """
    # for page in manager.collection('Cat').paginate(find={'name': 1}, size=5):
    #     print(len(page))
    #     for test in page:
    #         print(test)
    #
    assert True


def test_delete_single():
    owner = manager.collection('Owner').find_one({'name': 'Schrödinger'})
    assert owner is not None
    manager.remove(owner)
    assert owner.is_new()
