# Module Planner

## Installation

Make sure you have the following installed before continuing:

    - git
    - python2-pip
    - virutalenv
    - mongodb

If you haven't done so already clone the repository by running:
```
    $ git clone https://github.com/alcarney/moduleplanner-django.git
```

Then ```cd``` into your newly cloned repository and create a new virtual env
```
    $ virtualenv env
```

Activate your newly created virtualenv
```
    $ source env/bin/activate
```
You can check that this worked by running ```which python ``` which prints to the
shell the filepath of the python binary it should end with
```
    path/to/cloned/repo/env/bin/python
```

This next command will then install django and the other python dependencies needed for
this project into your virtualenv
```
    $ pip install -r requirements.txt
```

## Running the development server

Once you have everything you need installed and ready to go you can fire up the development server
by navigating to the ```bin``` directory and running
```
$ ./rundevserver.sh
```
__Note:__ Currently before running this command you have to create the directory ```module_planner/db/ ```
for this command to work this will be changed in the future so that this step is not necessary

# Contributors

    - Alex
    - Timothy
    - Adam
    - Vince
    - James
    - Json


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
