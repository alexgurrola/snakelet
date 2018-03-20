import configparser

from snakelet.storage import Document, Manager


class Test(Document):
    pass


def get_manager():
    # Read Configuration
    config = configparser.ConfigParser()
    config.read('tests/config.ini')
    config = config['storage']

    # Connect to Database
    manager = Manager(
        case='camel',
        database=config['db'],
        host=config['host'],
        port=config.getint('port'),
        username=config['user'],
        password=config.get('pass', raw=True)
    )

    # Register Types
    manager.register(Test)

    # Output
    return manager


def test_find():
    # Connection
    manager = get_manager()

    # Fetch and/or Create
    fetched = manager.Test.find_one({'name': 'example'})
    if not fetched:
        print('unable to find document; creating new document...')
        created = Test()
        created['name'] = 'example'
        print('save:', created)
        manager.save(created)
        print('persistent:', created)
    elif 'updated' not in fetched or not fetched['updated']:
        print('updating:', fetched)
        fetched['updated'] = True
        manager.save(fetched)
    else:
        print('fetched:', fetched)
        print('removing document...')
        manager.remove(fetched)


def test_page():
    # Connection
    manager = get_manager()

    # Settings
    """
    results = manager.Test.find({'name': 1})
    result_count = results.count()
    """
    result_count = manager.Test.collection.count()
    print('count:', result_count)

    if result_count < 10:
        filler = []
        for x in range(0, 10):
            data = Test({'value': x})
            filler.append(data)
            manager.save(data)

    for page in manager.Test.paginate(find={'name': 1}):
        for test in page:
            print(test)


if __name__ == '__main__':
    try:
        test_page()
    except KeyboardInterrupt:
        print('\nGoodbye!')
