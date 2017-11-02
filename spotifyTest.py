#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:27:14 2017

@author: deaxman
"""

#%%
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
planets = sns.load_dataset('planets')
titanic = sns.load_dataset('titanic')
exercise = sns.load_dataset('exercise')
#%%
import spotipy
#%%
spot=spotipy.Spotify()
results=spot.search('artist:Coldplay',type='artist')
artist_uri=results['artists']['items'][0]['uri']
for track in spot.artist_top_tracks(artist_uri)['tracks']:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print('popularity: ' + str(track['popularity']))
    
#%%
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import spotipy
import spotipy.util as util
#%%
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id='2b5c799785174aeaa6832663cf59e0cb',client_secret='91cb63d2f78847b78f3a9b4a76caa042')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))

playlists = sp.user_playlists('1260753194')

        
results = sp.user_playlist('1260753194', [i['id'] for i in playlists['items'] if i['name']=="Starred"][0],fields="tracks,next")
#results = sp.user_playlist('1260753194', [i['id'] for i in playlists['items'] if i['name']=="Starred"][0],fields="tracks")

tracks = results['tracks']
allNames=[]
allDates=[]
allPopularities=[]
while tracks['next']:
    for track in tracks['items']:
        allNames.append(track['track']['name'])
        allPopularities.append(track['track']['popularity'])
        allDates.append(track['added_at'])
    tracks = sp.next(tracks)
starredData=pd.DataFrame()
starredData['Name']=pd.Series(allNames)
starredData['Popularity']=pd.Series(allPopularities)
starredData['DateAdded']=pd.to_datetime(pd.Series(allDates))
sortedStarredData=starredData.sort('DateAdded')

