# User Guide

This is the User Guide for the Hackathon Starter Kit. Here you will find additional documentation and guides on how to use the project.

If you think we are missing something or you have ideas for more guides that should be on this page, [let us know](mailto:hi@mlh.io) or [contribute some](/contributing)!

## How It Works

This project simply provides the boilerplate to get started with a new Flask application. It provides the tools and guides to get started quickly. You can use this project as a starting point to building new applications during a hackathon.

Even if you are not using it for a hackathon, it should save you time getting started building and learning Flask development.


## Starting the app

You can run your application from your terminal using the `flask` command. To run the app locally, you need to tell Flask where to find your application, then run it in development mode.

Development mode makes it easier to make changes to your application. It includes an interactive debugger and will restart the server whenever you make changes to the code.

For Linux and Mac:

```
export FLASK_APP=app/app.py
export FLASK_ENV=development
flask run
```

For Windows Powershell, use `$env:` instead of `export`:

```
$env:FLASK_APP = 'app/app.py'
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
└── app/
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

The core of the Flask app is contained within the `app` directory. It contains `app.py`, the code to create and run the app, `/views`, handles all the endpoints and business logic, `/models`, handles all the features for the data models like users, `/templates`, contains the templates for [Jinja](http://jinja.pocoo.org/docs/2.10/)-based layouts, and `/static`, contains all the static assets. You can learn more about [the structure of Flask apps here](http://flask.pocoo.org/docs/1.0/tutorial/layout/).

## Flask Development

Flask is a "microframework" for developing web applications in Python. That means it is easy to get started with a basic application without a lot of boilerplate. This also means it relies heavily on external libraries, or extensions, to add new functionality. You can learn more about how to use Flask with [this guide](http://flask.pocoo.org/docs/1.0/tutorial/).

## OAuth Authentication

This project uses GitHub OAuth to handle user authentication. Meaning a new user of your site will sign in with a GitHub account instead of a new username and password. This typically is more secure because you won't be storing new credentials for each user. It is also quicker and easier for the user. Win-win.

The tradeoff is that you have to go through the [GitHub OAuth flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/) with your application. This process is pretty simple:

1. Users clicked **Sign in with GitHub**.
2. Users are redirected to GitHub.com to request their identity.
3. Users grant permission to your app and are redirected back to your site.
4. Your app sends a request for the user access token.
5. Your app uses GitHub's API with the stored access token.

The code that handles this process is contained in `views/auth.py` and `services/github.py`.
To use this authentication technique you need to setup a new GitHub OAuth app. [Instructions listed below](#github-oauth).

## Fetching Data

This project uses Python's `[requests](http://docs.python-requests.org/en/master/)` package to make HTTP requests. An example request in your terminal will look like this:

```
$ python
>>> import requests
>>> r = requests.get("https://api.github.com/repositories")
>>> print(r.json())
... Prints out results from GitHub
```

These type of requests can be made inside of your views to fetch and store data for your application. For example, you might make a request to GitHub's API and display it [directly in HTML](/github). Depending on your needs, you can also store this data to your database to use later.

To make things simple, we provide a service for GitHub-related requests, which will handle user authentication. Here is that [service in action](https://github.com/nlaz/github-hackathon-starter/blob/master/app/views/github.py).

## Static Files

Flask automatically adds a `static` view that serves files located in the `/static` folder. This folder is typically reserved for static files like CSS stylesheets, JavaScript files, images, or other assets. The folder currently has some default files to get started.

```
static/
├── vendor/
│   └── markdown.min.css
├── favicon.ico
└── style.css
```

The `style.css` file is a good place to add custom CSS. The `markdown.min.css` handles some default styling for the markdown guides for the project. Add any of your CSS or JavaScript in this folder.

## Saving to a Database

### Using Postgres
Flask does not come with a database layer by default. It is designed to have a database added later. You can add your own preferred database type to the project if needed. We like the PostgreSQL database which is easy to deploy with Heroku.

To use PostgreSQL with your project, you will need to [install it locally](https://wiki.postgresql.org/wiki/What's_new_in_PostgreSQL_9.4).

1. Install [Postgres locally](https://wiki.postgresql.org/wiki/What's_new_in_PostgreSQL_9.4)*
2. Make sure Postgres is running locally.
3. Replace the `DATABASE_URL` variable in `.env` with your database.
    * i.e. `DATABASE_URL=postgresql://localhost:5432/mlh-hackathon-flask-starter`

\* A simple way for Mac OS X users to install Postgres is using [Postgres.app](https://postgresapp.com/).

### Flask-SQLAlchemy

This project uses [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/) for interacting with the database layer. It is a Flask extension that adds support for [SQLAlchemy](https://www.sqlalchemy.org/) to your application. It is a simple ORM for Python that allows us to make SQL requests in Python. This means instead of writing SQL directly, we can call Python-based methods. Here is an example of creating and saving a user:

```
user = User(username='guest', email='guest@example.com')
db.session.add(user)
db.session.commit()
```

This gives us flexibility in our database layer and keeps our Python code clean of SQL commands. The data models located in the `/models` directory each use the `SQLAlchemy` library.

## <a name='github-oauth'>GitHub OAuth Apps</a>

This project uses a GitHub OAuth app for Authentication and uses GitHub's API. To setup GitHub for authentication, following these steps:

1. Register an account on Github.com.
2. Visit the [GitHub OAuth apps page](https://github.com/settings/developers).
3. Create a new OAuth app.
    * Enter an application name and a homepage URL.
    * Add callback URL, use http://localhost:5000/ for local development.
    * Click 'Register application'.
4. Add your GitHub credentials to your environment variables in `.env`.
    * Replace `[INSERT_CLIENT_ID]` with your GitHub Client ID.
    * Replace `[INSERT_CLIENT_SECRET]` with your GitHub Client Secret.

## <a name='environment-variables'>Environment Variables</a>
To run the project, you need to configure the application to run locally. This will require updating a set of environment variables specific to your environment. Create a new file named `.env` by duplicating `.env.sample`. Update the new file with the GitHub credentials. It should look similar to this:

```
# .env file
DATABASE_URL="[INSERT_DATABASE_URL]"
GITHUB_CLIENT_ID="[INSERT_CLIENT_ID]"
GITHUB_CLIENT_SECRET="[INSERT_CLIENT_SECRET]"
```

The `DATABASE_URL` variable is the path to your database system. This is where you can add the url to your PostgreSQL.

The `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` variables are the app credentials from your [GitHub OAuth app](https://github.com/settings/developers).


```
# .flaskenv file
FLASK_APP='app/app.py'
FLASK_ENV='development'
```

The `FLASK_APP` and `FLASK_ENV` variables are needed for running the application locally. The `SECRET_KEY` variable is used to manage the server sessions.


## Deployment

### Deploy to Heroku

Heroku is an easy way for developers to deploy their application. To deploy to Heroku, make sure you have the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed first. Then follow these steps:

1. Clone the code into a fresh folder: `git clone https://github.com/MLH/mlh-hackathon-flask-starter.git`
2. Navigate to the new folder: `cd mlh-hackathon-flask-starter`
3. Create a new Heroku app: `heroku create`
4. Push the code to Heroku with git: `git push heroku master`
5. Make sure the app builds and you can open it: `heroku open`

Alternatively, you can use this button to create a new application on Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/nlaz/mlh-hackathon-flask-starter)


# Support

If you are having problems running the project or getting it to work, check the [issue tracker](https://github.com/MLH/mlh-hackathon-flask-starter/issues) for any related issues. It might also have the solution to your issue. If an issue doesn't already exist, feel free to open a new issue. We will try to respond as quickly as possible.

You can also reach out to [our email](mailto:hi@mlh.io) to help with more pressing issues.
