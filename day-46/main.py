from billboard import GetBillboardSongs
from spotify import TrackSearcher, PlaylistBrain


date = input('Input the date you want to travel to (format: YYYY-MM-DD): ')

top_songs = GetBillboardSongs(date)
playlist = PlaylistBrain()


playlist.spotify_user_playlist_create(playlist_name=f'{date} Billboard 100', public=False)


uri_list = []

for track, musician in top_songs.results.items():
#searching for the track in spotify database
    track = TrackSearcher(artist=musician, track=track)
    if track.uri_track == '':
        pass
    else:
        uri_list.append(track.uri_track)


playlist.add_tracks_to_playlist(uri_list)
print(f'{len(uri_list)} tracks were added into the playlist')

    