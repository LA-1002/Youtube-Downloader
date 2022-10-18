
import playlist_getter;
import video_downloader;
import mp3_converter
import os;
import sys

def PlaylistDown(playlist):
    videos = playlist_getter.playListIDs(playlist);
    path = "C:\\Users\\leonn\\Videos\\Youtube\\" #SET CUSTOM PATH IF YOU ARE NOT ME AND DOWNLOADED THIS :)
    num = 0
    while num  < len(videos):
        down = True;
        print('VIDEO %s : %s'%((num+1),videos[num]))
        stage = ('%s - '%(num+1))
        stage = '';
        down = video_downloader.downloadVideo(videos[num],path,stage)
        if (down[0] != False):
            os.sleep(5)
            num+=1;
        print('#'*4)
    print('#'*10)
    print('DOWNLOADED : %s VIDEOS'%num);
    print('#'*10)

def VideoDown(video):
    path = "C:\\Users\\leonn\\Videos\\Youtube\\" #SET CUSTOM PATH IF YOU ARE NOT ME AND DOWNLOADED THIS :)
    down = video_downloader.downloadVideo(video,path,'')
    print('DOWNLOADED : %s'%down[1])

def AudioDown(video):
    path = "C:\\Users\\leonn\\Videos\\Youtube\\" #SET CUSTOM PATH IF YOU ARE NOT ME AND DOWNLOADED THIS :)
    down = video_downloader.downloadVideo(video,path,'')
    back = mp3_converter.AudioConvert(down[1])
    if (back==True):
        print('DOWNLOADED AND CONVERTED : %s'%((down[1].split('.mp3'))[0]))


if __name__ == '__main__':
    if (sys.argv[1] == '-pl'):
        PlaylistDown(sys.argv[2])
    if (sys.argv[1] == '-video'):
        VideoDown(sys.argv[2])
    if (sys.argv[1] == '-audio'):
        AudioDown(sys.argv[2])
