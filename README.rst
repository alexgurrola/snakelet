snakelet
========

.. image:: https://api.codacy.com/project/badge/Grade/7d934f54cbd0438098601f376ed2d51a
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/alexgurrola/snakelet?utm_source=github.com&utm_medium=referral&utm_content=alexgurrola/snakelet&utm_campaign=Badge_Grade_Dashboard

.. image:: https://badge.fury.io/py/snakelet.svg
    :target: https://badge.fury.io/py/snakelet

.. image:: https://travis-ci.com/alexgurrola/snakelet.svg?branch=master
    :target: https://travis-ci.com/alexgurrola/snakelet

.. image:: http://img.shields.io/coveralls/alexgurrola/snakelet/master.svg
    :target: https://coveralls.io/r/alexgurrola/snakelet

.. image:: https://scrutinizer-ci.com/g/alexgurrola/snakelet/badges/quality-score.png?b=master
    :target: https://scrutinizer-ci.com/g/alexgurrola/snakelet/?branch=master

.. image:: https://scrutinizer-ci.com/g/alexgurrola/snakelet/badges/coverage.png?b=master
    :target: https://scrutinizer-ci.com/g/alexgurrola/snakelet/?branch=master

Snakelet is a Schema-less ORM-like system built in pure Python to reduce
redundancy with Mongo Native Drivers and Object Management.  This package
contains a very simple implementation and will need to be expanded upon
largely to remain relevant.

documents
---------

Registration only requires exposing the object to the Manager.

.. code-block:: python

    from snakelet.storage import Document, Manager

    class Cat(Document):
        pass

    manager = Manager(database='felines')
    manager.register(Cat)

managers
--------

Connecting to a database is fairly straightforward.

.. code-block:: python

    from snakelet.storage import Manager

    manager = Manager(
        database='felines',
        host='localhost',
        port=27017,
        username='admin',
        password='pass'
    )

By default, Managers build and fetch collections in snake case, but this
can be switched to camel case during instantiation.

.. code-block:: python

    from snakelet.storage import Manager

    manager = Manager(
        case='camel'
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

This feature set is fairly simple and has normal iterable bindings to ensure simple operation.

.. code-block:: python

    for page in manager.Cat.paginate(find={'name': 1}):
        for cat in page:
            print(cat['name'])
