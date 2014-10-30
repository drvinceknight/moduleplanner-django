# Module Planner

To be able to run code in this repository you need the following packages
installed (all for python 2.x):

    - Django v1.7.1
    - MongoDB v2.6.5
    - PyMongo v2.7.2
    - MongoEngine v0.8.7
    - django-extensions v1.4.4

# Contributors

    - Alex
    - Timothy
    - Adam
    - Vince
    - James
    - Json

# Installation

Run pip install virtualenv
Install mongodb
Run pip install -r requirements.txt
Make the folder `module_planner/db`

Navigate to /bin and run rundevserver.sh

# Tests

## Functional Tests

Functiontional tests are run using [selenium](http://selenium-python.readthedocs.org/).
For a good overview see: [http://chimera.labs.oreilly.com/books/1234000000754/](http://chimera.labs.oreilly.com/books/1234000000754/).

At the moment tests are being developed for Firefox and Chrome.
For them to work you need to have the ChromeDriver executable in your path.
One approach to this is to download from [http://chromedriver.storage.googleapis.com/index.html](http://chromedriver.storage.googleapis.com/index.html) and put the `ChromeDriver` file in a folder like `/usr/local/bin`.

To run the functional tests:

    $ python python functional_tests.py

This should open two browser windows: (one in chrome and the other in firefox).
No output on the shell is a good thing.

## Unit Tests
