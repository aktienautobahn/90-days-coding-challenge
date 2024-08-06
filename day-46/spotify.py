from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy
import sys
import pprint
import json

CLIENT_ID = ''
SPOTIFY_SECRET = ''
SCOPE = 'playlist-modify-private'



class TrackSearcher:
    def __init__(self, artist, track) -> None:
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=SPOTIFY_SECRET))
        self.artist = artist
        self.track = track
        self.uri_track = ''
        self.track_query()



    def track_query(self):

        result = self.sp.search(self.track, limit=2, type='track')['tracks']['items']
        for item in result:
            if item['artists'][0]['name'] == self.artist:
                self.uri_track = item['uri']




class PlaylistBrain:
    def __init__(self) -> None:
        
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://example.com",
                client_id=CLIENT_ID,
                client_secret=SPOTIFY_SECRET,
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        self.user_id = self.sp.current_user()["id"]


    
    def spotify_user_playlist_create(self, playlist_name, public=True, collaborative=False, description=''):

        """Creates a playlist for a user

        Parameters:
        user - the id of the user
        name - the name of the playlist
        public - is the created playlist public
        collaborative - is the created playlist collaborative
        description - the description of the playlist
        """


        self.created_playlist = self.sp.user_playlist_create(self.user_id, playlist_name, public, collaborative, description)
        print(f"Playlist '{self.created_playlist['name']}' created.")


    def get_user_playlists(self, limit=50, offset=0):
        """Gets playlists of a user

        Parameters:
        user - the id of the user
        limit - the number of items to return
        offset - the index of the first item to return
        """
        

        return self.sp.user_playlists(self.user_id, limit, offset)


    
    def add_tracks_to_playlist(self, tracks):
        """Adds tracks/episodes to a playlist

        Parameters:
        playlist_id - the id of the playlist
        items - a list of track/episode URIs, URLs or IDs
        position - the position to add the tracks
        """
        self.sp.user_playlist_add_tracks(self.user_id, self.created_playlist['id'], tracks, position=None)


