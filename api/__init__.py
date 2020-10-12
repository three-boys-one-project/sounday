CONCURRENT_POOL = 10

SPOTIFY_API_RETRIES = 3
SPOTIFY_API_RTD = 5
SPOTIFY_API_TIMEOUT = 15
SPOTIFY_RESPONSE_TYPE = 'code'
SPOTIFY_REDIRECT_URI = 'http://127.0.0.1:8000' #CHANGE WHEN DEPLOYED
SPOTIFY_SCOPES = 'playlist-modify-private playlist-modify-public'
SPOTIFY_API_LOGIN_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_API_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_API_CURRENT_USER = 'https://api.spotify.com/v1/me'
SPOTIFY_API_CREATE_PLAYLIST = 'https://api.spotify.com/v1/users/{user_id}/playlists'
SPOTIFY_API_SEARCH = 'https://api.spotify.com/v1/search'
SPOTIFY_API_ADD_TRACKS = 'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

MESSAGE_ERROR = 'Unexpected error.'
MESSAGE_USER_NOT_FOUND = 'User not found.'
MESSAGE_REPOS_NOT_FOUND = 'You should have at least one public repository.'
MESSAGE_TOKEN_NOT_FOUND = 'Error while retrieving the Spotify token.'
MESSAGE_SPOTIFY_NOT_FOUND = 'Spotify user not found.'
MESSAGE_SPOTIFY_PLAYLIST_ERROR = 'Spotify playlist cannot be created.'
MESSAGE_COMMIT_NOT_FOUND = 'Any commit could be retrieved.'
MESSAGE_SPOTIFY_TRACK_ERROR = 'Spotify tracks cannot be created.'

NLP_MOST_COMMON_K = 25

__all__ = [
    'CONCURRENT_POOL',
    'NLP_MOST_COMMON_K',
    'SPOTIFY_API_RETRIES',
    'SPOTIFY_API_RTD',
    'SPOTIFY_API_TIMEOUT',
    'SPOTIFY_RESPONSE_TYPE',
    'SPOTIFY_REDIRECT_URI',
    'SPOTIFY_SCOPES',
    'SPOTIFY_API_LOGIN_URL',
    'SPOTIFY_API_TOKEN_URL',
    'SPOTIFY_API_CURRENT_USER',
    'SPOTIFY_API_CREATE_PLAYLIST',
    'SPOTIFY_API_SEARCH',
    'SPOTIFY_API_ADD_TRACKS',
    'MESSAGE_ERROR',
    'MESSAGE_USER_NOT_FOUND',
    'MESSAGE_REPOS_NOT_FOUND',
    'MESSAGE_TOKEN_NOT_FOUND',
    'MESSAGE_SPOTIFY_NOT_FOUND',
    'MESSAGE_SPOTIFY_PLAYLIST_ERROR',
    'MESSAGE_COMMIT_NOT_FOUND',
    'MESSAGE_SPOTIFY_TRACK_ERROR'
]