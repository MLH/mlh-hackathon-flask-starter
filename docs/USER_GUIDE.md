# User Guide

This is the User Guide for the Hackathon Starter Kit. Here you will find additional documentation and guides on how to use the project.

If you think we are missing something or you have ideas for more guides that should be on this page, [let us know]() or [contribute some](/contributing)!

## How It Works

This project simply provides the boilerplate to get started with a new Flask application. It provides the tools and guides to get started quickly. You can use this project as a starting point to building new applications during a hackathon.

Even if you are not using it for a hackathon, it should save you time getting started building and learning Flask development.


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

Flask is a "microframework" for developing web applications in Python. That means it is easy to get started with a basic application without a lot of boilerplate. This also means it relies heavily on external libraries, or extensions, to add new functionality.

## GitHub

This project uses GitHub for Authentication and uses GitHub's API. To setup GitHub for authentication, following these steps:

1. Register an account on Github.com.
2. Visit the [GitHub OAuth apps page](https://github.com/settings/developers).
3. Create a new OAuth app.
    * Enter an application name and a homepage URL.
    * Add callback URL, use http://localhost:5000/ for local development.
    * Click 'Register application'.
4. Add your GitHub credentials to your environment variables in `.env`.
    * Replace `<INSERT_CLIENT_ID>` with your GitHub Client ID.
    * Replace `<INSERT_CLIENT_SECRET>` with your GitHub Client Secret.

# Support

If you are having problems running the project or getting it to work, check the [issue tracker](https://github.com/MLH/mlh-hackathon-flask-starter/issues) for any related issues. It might also have the solution to your issue. If an issue doesn't already exist, feel free to open a new issue. We will try to respond as quickly as possible.

You can also reach out to our email to help with more pressing issues.
