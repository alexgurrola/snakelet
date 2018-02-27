snakelet
========

.. image:: https://badge.fury.io/py/snakelet.svg
    :target: https://badge.fury.io/py/snakelet

Snakelet is a Schema-less ORM-like system built in pure Python to reduce
redundancy with Mongo Native Drivers and Object Management.  This package
contains a very simple implementation and will need to be expanded upon
largely to remain relevant.

documents
---------

Registration only requires exposing the object to the Manager.

.. code-block:: python

    from snakelet.storage.document import Document
    from snakelet.storage.manager import Manager

    class Cat(Document):
        pass

    manager = Manager(database='felines')
    manager.register(Cat)

managers
--------

Connecting to a database is fairly straightforward.

.. code-block:: python

    from snakelet.storage.manager import Manager

    manager = Manager(
        database='felines',
        host='localhost',
        port=27017,
        username='admin',
        password='pass'
    )

Finding, Saving, and Removal are also pretty straightforward.

.. code-block:: python
    pye = manager.Cat.find_one({'name': 'pyewacket'})
    shoshana = Cat()
    shoshana['name'] = 'shoshana'
    shoshana['owner'] = 'schrodinger'
    manager.save(shoshana)
    schrodinger = manager.Cat.find({'owner': 'schrodinger'})
    manager.remove(pye)

pagination
----------

This feature is already built, so the example will be coming soon!