# Introduction

This is a hackathon boilerplate for new Flask web applications created by [Major League Hacking](https://github.com/MLH). It is for hackers looking to get started quickly on a new hackathon project using the Flask microframework.

* [Installation Guide](#installation-guide) - How to get started with a new Flask app
* [User Guide](/user-guide) - How to develop apps created with this starter project
* [Contributing Guide](/contributing) - How to contribute to the project

# <a name='installation-guide'>Installation Guide</a>

This project requires the following tools:

* Python ([3.4](https://www.python.org/downloads/)) - The programming language used by Flask.
* PostgreSQL ([9.4](https://wiki.postgresql.org/wiki/What's_new_in_PostgreSQL_9.4)) - A relational database system.
* Virtualenv - A tool for creating isolated Python environments.

To get started, install Python and Postgres on your local computer, if you don't have them already. A simple way for Mac OS X users to install Postgres is using [Postgres.app](https://postgresapp.com/). You can optionally use another database system instead of Postgres, like [SQLite](http://flask.pocoo.org/docs/1.0/patterns/sqlite3/).

## Installation

**1. Clone this repository to your local computer.**

```
$ git clone https://github.com/MLH/github-hackathon-starter.git
$ cd github-hackathon-starter
```

**2. Create and activate a [virtual environment](http://flask.pocoo.org/docs/1.0/installation/#virtual-environments).**

```
$ python3 -m venv venv
$ . venv/bin/activate
```

**3. Install Flask dependencies using `pip`.**

```
$ pip install -r requirements.txt
```


## Starting the app

You can run your application from your terminal using the `flask` command. To run the app locally, you need to tell Flask where to find your application, then run it in development mode.

Development mode makes it easier to make changes to your application. It includes an interactive debugger and will restart the server whenever you make changes to the code.

For Linux and Mac:

```
export FLASK_APP=starter
export FLASK_ENV=development
flask run
```

For Windows Powershell, use `$env:` instead of `export`:

```
$env:FLASK_APP = 'starter'
$env:FLASK_ENV = 'development'
flask run
```

### `flask run`

Runs the app in development mode. Requires the `FLASK_APP` and `FLASK_ENV` variables to be set.
Opens http://localhost:5000 to view it in your browser.

The app will automatically reload if you make changes to the code.
You will see the build errors and warnings in the console.

### `pip install`

Installs a Python package for your application. Used to add new functionality to the project.

# What's Included?

* [Flask](http://flask.pocoo.org/) - A microframework for Python web applications
* [Flask Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/) - A Flask concept for making modular applications
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - A Flask extension that adds ORM support for your data models.
* [Flask-Misaka](https://flask-misaka.readthedocs.io) - A Flask extension that supports rendering markdown into HTML.
* [Werkzeug](http://werkzeug.pocoo.org/) - A Flask framework that implements WSGI for handling server requests.
* [Bootstrap 4](https://getbootstrap.com/) - An open source design system for HTML, CSS, and JS.
* [Jinja2](http://jinja.pocoo.org/docs/2.10/) - A templating language for Python, used by Flask.

# Code of Conduct

The [MLH Code of Conduct](https://static.mlh.io/docs/mlh-code-of-conduct.pdf) applies to project participants and we expect contributors and maintainers to adhere to this standard.

# License

The Hackathon Starter Kit is open source software [licensed as MIT](https://github.com/nlaz/github-hackathon-starter/blob/master/LICENSE.md).
