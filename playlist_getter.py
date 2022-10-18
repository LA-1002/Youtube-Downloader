import requests
import os

type = 'playlists';
key = os.environ['YTAPI']
part = 'contentDetails'



def getPlaylistNumber(playlist):
    url = ('https://youtube.googleapis.com/youtube/v3/playlistItems?key=%s&playlistId=%s&part=%s'%(key,playlist,part))
    req = requests.get(url);
    results = req.json()['pageInfo']['totalResults']
    print(results);

def playListIDs(playlistID):
    url = ('https://youtube.googleapis.com/youtube/v3/playlistItems?key=%s&playlistId=%s&part=%s&maxResults=50'%(key,playlistID,part));
    req = requests.get(url);
    items = req.json()['items']
    file = open('Video_URLs.txt','w')
    videos = [];
    for i in items:
        id = (i['contentDetails']['videoId'])
        url = ('https://www.youtube.com/watch?v=%s'%id);
        file.write(('https://www.youtube.com/watch?v=%s \n\n'%id));
        videos.append(url)
    return videos;
    #file.close();






