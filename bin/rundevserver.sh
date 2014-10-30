#!/bin/bash

# Change to project root and activate the virtualenv
echo "\t=> Activating Virtualenv"
cd ../
source env/bin/activate

# Descend into the module_planner and start mongodb
echo "\t=> Starting MongoDB Server"
cd module_planner/
mongod --dbpath db --smallfiles &
sleep 5

# Start python development server
echo "\t=> Starting Development Server"
python manage.py runserver
