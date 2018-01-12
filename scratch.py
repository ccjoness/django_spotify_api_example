# import sys
# import spotipy
# import spotipy.util as util
#
# scope = 'user-library-read'
#
# # if len(sys.argv) > 1:
# #     username = sys.argv[1]
# # else:
# #     print("Usage: %s username" % (sys.argv[0],))
# #     sys.exit()
# username = 'chris.charles.jones@gmail.com'
#
# token = util.prompt_for_user_token(username, scope)
#
# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", username)


result = {
    'added_at': '2018-01-01T23:45:34Z',
    'track': {
        'album': {
            'album_type': 'album',
            'artists': [{
                'external_urls': {
                    'spotify': 'https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02'
                },
                'href': 'https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02',
                'id': '06HL4z0CvFAxyc27GXpf02',
                'name': 'Taylor Swift',
                'type': 'artist',
                'uri': 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
            }],
            'available_markets': [
                'AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO',
                'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY',
                'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES',
                'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN',
                'HU', 'ID', 'IE', 'IS', 'IT', 'JP', 'LI',
                'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY',
                'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH',
                'PL', 'PT', 'PY', 'SE', 'SG', 'SK', 'SV',
                'TH', 'TR', 'TW', 'US', 'UY', 'VN'
            ],
            'external_urls': {
                'spotify': 'https://open.spotify.com/album/6DEjYFkNZh67HP7R9PSZvv'
            },
            'href': 'https://api.spotify.com/v1/albums/6DEjYFkNZh67HP7R9PSZvv',
            'id': '6DEjYFkNZh67HP7R9PSZvv',
            'images': [
                {
                    'height': 640, 'url': 'https://i.scdn.co/image/abd96549fa53000a633d64cbab5a69a623b6bdfa',
                    'width': 640
                },
                {
                    'height': 300, 'url': 'https://i.scdn.co/image/22692a034870c105fc45278228cd79898332b170',
                    'width': 300
                },
                {
                    'height': 64, 'url': 'https://i.scdn.co/image/cfeb3b01855b8266d15fe578181c3905b4485d58', 'width': 64
                }],
            'name': 'reputation',
            'type': 'album',
            'uri': 'spotify:album:6DEjYFkNZh67HP7R9PSZvv'},
        'artists': [
            {
                'external_urls': {
                    'spotify': 'https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02'
                },
                'href': 'https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02',
                'id': '06HL4z0CvFAxyc27GXpf02',
                'name': 'Taylor Swift',
                'type': 'artist',
                'uri': 'spotify:artist:06HL4z0CvFAxyc27GXpf02'}],
        'available_markets': [
            'AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR',
            'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE',
            'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB',
            'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IS',
            'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT',
            'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE',
            'PH', 'PL', 'PT', 'PY', 'SE', 'SG', 'SK', 'SV',
            'TH', 'TR', 'TW', 'US', 'UY', 'VN'
        ],
        'disc_number': 1,
        'duration_ms': 207133,
        'explicit': False,
        'external_ids': {
            'isrc': 'USCJY1750014'
        },
        'external_urls': {
            'spotify': 'https://open.spotify.com/track/07NxDD1iKCHbAldceD7QLP'
        },
        'href': 'https://api.spotify.com/v1/tracks/07NxDD1iKCHbAldceD7QLP',
        'id': '07NxDD1iKCHbAldceD7QLP',
        'name': 'This Is Why We Can’t Have Nice Things',
        'popularity': 74,
        'preview_url': 'https://p.scdn.co/mp3-preview/57df9c0b435edd8d0936c12abbd779ff30666a53?cid=d85ad5c1e6b44116935bf44620736188',
        'track_number': 13, 'type': 'track',
        'uri': 'spotify:track:07NxDD1iKCHbAldceD7QLP'
    }}
