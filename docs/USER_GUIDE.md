# User Guide

This is the User Guide for the Hackathon Starter Kit. Here you will find additional documentation and guides on how to use the project.

## How It Works

## Starting the app

You can run your application from your terminal using the `flask` command. To run the app locally, you need to tell Flask where to find your application, then run it in development mode.

Development mode makes it easier to make changes to your application. It includes an interactive debugger and will restart the server whenever you make changes to the code.

For Linux and Mac:

```
export FLASK_APP=project_name
export FLASK_ENV=development
flask run
```

For Windows Powershell, use `$env:` instead of `export`:

```
$env:FLASK_APP = 'project_name'
$env:FLASK_ENV = 'development'
flask run
```

### `flask run`

Runs the app in development mode. Requires the `FLASK_APP` and `FLASK_ENV` variables to be set.
Open http://localhost:5000 to view it in your browser.

The app will automatically reload if you make changes to the code.
You will see the build errors and warnings in the console.

### `pip install`

Installs a Python package for your application. Used to add new functionality to the project.

## Project Structure

```
mlh-hackathon-flask-starter/
├── README.md
├── Procfile
├── requirements.txt
├── setup.py
├── build/
├── docs/
└── project_name/
  ├── views/
  │   ├── auth.py
  │   ├── github.py
  │   └── public.py
  ├── models/
  │   └── user.py
  ├── services/
  │   └── github.py
  ├── static/
  │   ├── vendor/
  │   └── style.css
  ├── templates/
  │   ├── github/
  │   └── home/
  ├── app.py
  ├── extensions.py
  └── settings.py
```

The core of the Flask app is contained within the `project_name` directory. It contains `app.py`, the code to create and run the app, `/views`, handles all the endpoints and business logic, `/models`, handles all the features for the data models like users, `/templates`, contains the templates for [Jinja](http://jinja.pocoo.org/docs/2.10/)-based layouts, and `/static`, contains all the static assets. You can learn more about [the structure of Flask apps here](http://flask.pocoo.org/docs/1.0/tutorial/layout/).

## Flask Development
* Application Setup
* Templates
* Blueprints and Views
* Static Files
* Using the Database
* Flash Messages

## Guides

### GitHub
* Setting up OAuth apps, authentication, etc.
* Fetching and using GitHub's API

### PostgreSQL
* Setting up database
* Inserting and running commands

# Deployment
* Deploy to Heroku
* Deploy to Google Cloud Platform
* Deploy using Docker

# Support
* Troubleshooting
* Support channel for hackathons
* Filing issues
* Contact email
