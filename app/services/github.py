import requests, json

api_url = 'https://api.github.com'
authorize_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

class GitHub():

    def __init__(self, client_id = '', client_secret = '', access_token = ''):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token

    def authorization_url(self, scope):
        return authorize_url + '?client_id={}&client_secret={}&scope={}'.format(
            self.client_id,
            self.client_secret,
            scope
        )

    def get_token(self, code):
        """Fetch GitHub Access Token for GitHub OAuth."""
        headers = { 'Accept': 'application/json' }
        params = {
            'code': code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }

        data = requests.post(token_url, params=params, headers=headers).json()
        return data.get('access_token', None)

    def get(self, route_url, params = {}):
        url = api_url + route_url
        params['access_token'] = self.access_token

        return requests.get(url, params=params).json()

    def post(self, route_url, params = {}):
        url = api_url + route_url
        params['access_token']  = self.access_token

        return requests.post(url, params=params).json()

    def delete(self, route_url, params = {}):
        url = api_url + route_url
        params['access_token']  = self.access_token

        return requests.delete(url, params=params)

    @staticmethod
    def get_user_from_token(access_token):
        """Fetch user data using the access token."""
        url = api_url + '/user'
        params = { 'access_token': access_token }

        return requests.get(url, params=params).json()
