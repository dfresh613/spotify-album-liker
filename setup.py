from setuptools import setup

setup(
    name="spotify-albumliker",
    description="Automatically add songs from your Spotify followed albums into 'all songs'",
    long_description="Miss the old Spotify UI in which you could see all of your songs in a "
                     "single location? Want to listen to all songs of your"
                     " liked albums alongside your individually liked songs? This script is for you!",
    version='1.0',
    py_modules=['spotify_album_liker'],
    install_requires=[
        'click',
        'spotipy'
    ],
    entry_points='''
        [console_scripts]
        spotifyliker=spotify_album_liker:cli
    ''',
)