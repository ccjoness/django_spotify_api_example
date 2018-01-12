from django.shortcuts import render, HttpResponseRedirect
import spotipy
import spotipy.util as util
from spotipy import oauth2
scope = 'user-library-read'
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = ''
username = ''
# Create your views here.


def next_offset(n):
    try:
        return int(n['next'].split('?')[1].split('&')[0].split('=')[1])
    except ValueError:
        return None
    except AttributeError:
        return None
    except TypeError:
        return None


def home(request):
    return render(request, 'pages/home.html', {})


def sign_in(request):

    # token = util.prompt_for_user_token(username, scope)
    # print(token)
    sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,
                                   scope=scope, cache_path=".cache-" + username)
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        return HttpResponseRedirect(auth_url)
    sp = spotipy.Spotify(auth=token_info['access_token'])
    total = []
    results = sp.current_user_saved_tracks(limit=50)
    next = next_offset(results)

    total.append(results)
    while next and next < int(results['total']):
        next_50 = sp.current_user_saved_tracks(limit=50, offset=next)
        next = next_offset(next_50)
        total.append(next_50)
        print(next)
    tracks = []
    for r in total:
        for track in r['items']:
            tracks.append(track)

    return render(request, 'pages/sign-in.html', {'results': tracks})


def after_sign_in(request):
    results = {}
    token = 'http://localhost:8000/after-sign-in/?{}'.format(request.GET.urlencode())
    sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,
                                   scope=scope, cache_path=".cache-" + username)
    code = sp_oauth.parse_response_code(token)
    token_info = sp_oauth.get_access_token(code)
    if token_info:
        sp = spotipy.Spotify(auth=token_info['access_token'])
        results = sp.current_user_saved_tracks()
    return render(request, 'pages/sign-in.html', {'results': results['items']})
