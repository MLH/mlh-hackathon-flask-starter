from flask import flash

import requests
import json

class GitHub():

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token(self, code):
        """Fetch GitHub Access Token for GitHub OAuth."""
        url = 'https://github.com/login/oauth/access_token'
        headers = { 'Accept': 'application/json' }
        params = {
            'code': code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }

        response = requests.post(url, params=params, headers=headers)
        data = response.json()

        if not 'access_token' in data:
            # Issue in retrieving GitHub access token
            flash('Could not authorize your request. Please try again.')
            return '', 404

        return data['access_token']

    def get_user_from_token(access_token):
        """Fetch user data using the access token."""
        url = 'https://api.github.com/user'
        params = { 'access_token': access_token }

        response = requests.get(url, params=params)
        return response.json()

    def get_starred_repos(access_token):
        """Fetch starred repos for current user"""
        url = 'https://api.github.com/user/starred'
        params = { 'access_token': access_token }

        response = requests.get(url, params=params)
        return response.json()

    def search_repos(access_token, search):
        """Fetch repos that match search string"""
        url = 'https://api.github.com/search/repositories'
        params = { 'q': search, 'access_token': access_token }

        response = requests.get(url, params=params)
        return response.json()

    def unstar_repo(access_token, repo_name):
        """Unstars the repo if specified for the current user"""
        url = 'https://api.github.com/user/starred/{}'.format(repo_name)
        params = { 'access_token': access_token }

        response = requests.delete(url, params=params)
        return response
