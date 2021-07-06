# Task App With Flask 
Task App Flask is a practice to create a simple application using Flask, which makes use of authentication for login.

It has a connection to a non-relational database which is Firestore from Google Cloud Platform.

### Functionalities of the application:
1. Register a user
1. Login
1. Create Task
1. Delete task
1. Update task

## How to use it
```bash
$ # Get the code
$ git clone https://github.com/josbp0107/task-app-flask.git
$ cd task-app-flask
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=main.py
$ (Windows) set FLASK_APP=main.py
$ (Powershell) $env:FLASK_APP = ".\main.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_DEBUG=1
$ # (Windows) set FLASK_DEBUG=1
$ # (Powershell) $env:FLASK_DEBUG = 1
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

## Code-base structure

The project is coded using blueprints

## How to colaborate
Fork the project and create a pull request

> I will be happy to receive improvements to this application that will help me to continue learning

