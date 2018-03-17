import configparser

from snakelet.storage import Document, Manager


class Test(Document):
    pass


def test_find():
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


if __name__ == '__main__':
    try:
        test_find()
    except KeyboardInterrupt:
        print('\nGoodbye!')
