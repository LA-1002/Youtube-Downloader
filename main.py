
import playlist_getter;
import video_downloader;
import os;

def YoutubeDown(playlist):
    playlist = 'PL590L5WQmH8dsxxz7ooJAgmijwOz0lh2H'
    videos = playlist_getter.playListIDs(playlist);
    path = "C:\\Users\\leonn\\Videos\\Youtube\\"
    num = 0
    while num  < len(videos):
        down = True;
        print('VIDEO %s : %s'%((num+1),videos[num]))
        stage = ('%s - '%(num+1))
        stage = '';
        down = video_downloader.downloadVideo(videos[num],path,stage)
        if (down != False):
            os.sleep(5)
            num+=1;
        print('#'*4)
    print('#'*10)
    print('DOWNLOADED : %s VIDEOS'%num);
    print('#'*10)


if __name__ == '__main__':
    print('YES');