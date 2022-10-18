from pytube import YouTube;
import time




def downloadVideo(url,path,stage):
    video = YouTube(url)
    print(video.streams);
    streams = video.streams.filter(file_extension='mp4').get_by_itag(18)
    print(streams)
    name = video.title.replace('|','-').replace('?','').replace(':','').replace('/','').replace('"','').replace('\\','').replace('>','').replace('<','').replace('*','');
    name = stage + name + '.mp4';
    channel = video.author+'\\'
    path = path+channel;
    streams.download(filename=name,output_path=path)
    time.sleep(2);
    return [True,name]

url = 'https://www.youtube.com/watch?v=N0NejD-fDns';

path = "C:\\Users\\leonn\\Videos\\Youtube\\"
#path = "C:\\Users\\leonn\\Videos\\"
#files = downloadVideo(url,path,'')
#print(files);

