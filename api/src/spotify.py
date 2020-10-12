from multiprocessing.dummy import Pool as ThreadPool

from src import *
from src.helper import response, log
from src.helper.timer import Timer
from src.services import spotify_api


def login():
    try:
        with Timer('Get Auth URL'):
            auth_url = spotify_api.get_auth_url()
        return response.make(error=False, response=dict(redirect=auth_url))
    except Exception as e:
        log.error(f'Exception while processing {login.__name__} function: [{e}]')
        log.exception(e)
        return response.make(error=True, message=MESSAGE_ERROR)


def playlist(code, text, title):
    try:
        with Timer('Request token retrieving'):
            access_token = spotify_api.get_access_token(code)
            if not access_token:
                return response.make(error=True, message=MESSAGE_TOKEN_NOT_FOUND)

        with Timer('Get profile data'):
            user_id = spotify_api.get_current_user_id(access_token)
            if not user_id:
                return response.make(error=True, message=MESSAGE_SPOTIFY_NOT_FOUND)

        with Timer('Playlist generation'):
            playlist_id, playlist_url = spotify_api.post_playlist(access_token, user_id, title)
            if not playlist_id and not playlist_url:
                return response.make(error=True, message=MESSAGE_SPOTIFY_PLAYLIST_ERROR)

        with Timer('Search for tracks'):
            with ThreadPool(CONCURRENT_POOL) as pool:
                lower_bound = 0
                upper_bound = len(text)-1
                words = text.split()
                thread_args = []
                while lower_bound < len(tex):
                    while upper_bound >= lower_bound:
                        thread_args.append(' '.join(words[lower_bound:upper_bound]))
                        upper_bound -= 1
                    lower_bound +=1 
                    upper_bound = len(text)-1
                track_uri_list = list(pool.imap(spotify_api.search_for_tracks, thread_args))
                track_uri_list = [t for t in track_uri_list if t]

        with Timer('Add tracks to the playlist'):
            success = spotify_api.add_tracks_to_playlist(access_token, playlist_id, track_uri_list)
            if not success:
                return response.make(error=True, message=MESSAGE_SPOTIFY_TRACK_ERROR)

        return response.make(error=False, response=dict(url=playlist_url))

    except Exception as e:
        log.error(f'Exception while processing {playlist.__name__} function: [{e}]')
        log.exception(e)
        return response.make(error=True, message=MESSAGE_ERROR)