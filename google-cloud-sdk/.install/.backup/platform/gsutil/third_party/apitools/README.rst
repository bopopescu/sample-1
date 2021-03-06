google-apitools
===============

.. image:: https://travis-ci.org/craigcitro/apitools.png?branch=master
        :target: https://travis-ci.org/craigcitro/apitools

``google-apitools`` is a collection of utilities to make it easier to build
client-side tools, especially those that talk to Google APIs.

**NOTE**: This library is stable, but in maintenance mode, and not under
active development. However, any bugs or security issues will be fixed
promptly.

Installing as a library
-----------------------

To install the library into the current virtual environment::

   $ pip install google-apitools

Installing the command-line tools
---------------------------------

To install the command-line scripts into the current virtual environment::

   $ pip install google-apitools[cli]

Running the tests
-----------------

First, install the testing dependencies::

   $ pip install google-apitools[testing]

and the ``nose`` testrunner::

   $ pip install nose

Then run the tests::

   $ nosetests
