Intro
=====

Welcome to ``rtd.calculator``. How to install using pip:

.. code-block:: bash

    $ pip install rtd.calculator


Usage
=====

.. ipython:: python
        :suppress:

        # setup some test data for this example
        import shutil
        import zipfile
        shutil.copy2("../pyproject.toml", ".")

.. ipython::

        In [1]: from rtd.calculator import operations

        In [2]: operations.add(1, 2)

        In [3]: operations.subtract(1, 2)

        In [4]: operations.multiply(1, 2)
