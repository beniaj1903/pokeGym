POKEGYM SERVER

 Project Description

This is a project that generates an endpoint that can be called from display of a pokemon gym, this server queues pokemon in local storage, and then when require sends 18 pokemons to the display, the pokemons ares sorted in alphabetical ascending order. It supports power interruptions of the server, in a way that the queue is not lost on failures.

 Client acces
 
To access the queue you must do a GET HTTP request of the endpoint "$serverhost/pokegym/entries", this endpoint returns the name and id of 18 pokemons in JSON format.
 
 Server access

To activate the server you must install a few features:

  - Python 3
Main core to run this server, to install this interpreter follow the instructions on this https://realpython.com/installing-python/, this includes the package manager pip, that we use to install the dependencies for this project

  - Pipenv
Extending the package managment, pipenv generates a local environment with the dependencies associated to the project, more about this and installation on https://pipenv-es.readthedocs.io/es/stable/

 Running the project
 
- Run the virtual environment with the command pipenv shell
- Run the main file app.py
- Now the server is running on http://localhost:5000/ or the defined host address for the server if changed
