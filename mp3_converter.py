from moviepy.editor import *

m4 = r'C:\Users\leonn\Videos\Youtube\kameko\Holiday - KSI (cover by kameko).mp4'

def AudioConvert(m4):
    sp = m4.split('.mp4');
    m3 = (r'%s'%(sp[0] + '.mp3'))
    video = VideoFileClip(m4);
    audio = video.audio
    audio.write_audiofile(m3)
    audio.close()
    video.close()




