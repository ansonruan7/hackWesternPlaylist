# import os
# from flask import Flask, request, url_for, session, redirect
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import time

# #Creates Flask application
# app = Flask(__name__)


# app.secret_key = "Meowmeowmeowmeow" #dw
# app.config['SESSION_COOKIE_NAME'] = 'Dogs Cookie'
# TOKEN_INFO = "token_info"

# @app.route('/')
# def login():
#     sp_oauth = create_spotify_oauth()
#     auth_url = sp_oauth.get_authorize_url()
#     return redirect(auth_url)

# @app.route('/redirect')
# def redirectPage():
#     sp_oauth = create_spotify_oauth()
#     session.clear()
#     code = request.args.get('code')
#     token_info = sp_oauth.get_access_token(code)
#     session[TOKEN_INFO] = token_info
#     return redirect(url_for('addSongs', _external=True))



# @app.route('/searchSpotify')
# def searchTracks():
#   #Needs to be changed to look like cohereGen.py
#     try:
#         token_info = get_token()
#     except:
#         print("User not logged in")
#         return redirect(url_for('login', _external=False))
#     sp = spotipy.Spotify(auth=token_info['access_token'])
#     b = sp.search("Good Time",1,0,"track",None)
#     return(b['tracks']['items'][0]['external_urls'])

# @app.route('/addToPlaylist')
# def addSongs(title): #Parameters (playlist, array of track uri(MUST be in an array))
#     login()
#     redirectPage()
#     try:
#         token_info = get_token() #Making sure token isn't expired
#     except:
#         print("User not logged in")
#         return redirect(url_for('login', _external=False)) #If expired go to login
#     sp = spotipy.Spotify(auth=token_info['access_token']) #Accessing user account
#     sp.playlist_add_items("spotify:playlist:25bhxptEEIHSOEGRUNBCj1",title,position=None)


# @app.route('/createNewPlaylist')
# def createPlaylist(): #Parameters (username, title, description)
#     username = "ice_jacky" #user grabs from spotify
#     title = "Hard Coded Title LMao"
#     description = "made with love"
#     try:
#         token_info = get_token()
#     except:
#         print("User not logged in")
#         return redirect(url_for('login', _external=False))
#     sp = spotipy.Spotify(auth=token_info['access_token'])
#     sp.user_playlist_create(username,title,True,False,description) #Change to parameters
#     addSongs() #Add parameters
#     return redirect(url_for('login', _external=True))



# def get_token():
#     token_info = session.get(TOKEN_INFO, None)
#     if not token_info:
#         raise "exception"
#     now = int(time.time())
#     is_expired = token_info['expires_at'] - now < 60
#     if(is_expired):
#         sp_oauth = create_spotify_oauth()
#         token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
#     return token_info


# def create_spotify_oauth():
#     return SpotifyOAuth(
#         client_id= os.environ['SPOTIPY_CLIENT_ID'],
#         client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
#         redirect_uri=url_for('redirectPage', _external=True),
#         scope = "playlist-modify-public, playlist-modify-private, user-library-modify"
#     )

# app.run(host='0.0.0.0', port=5000,debug=True)  # Run the Application (in debug mode),
