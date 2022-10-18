from moviepy.editor import *


def AudioConvert(m4):
    m4 = (r'%s'%(m4));
    sp = m4.split('.mp4');
    m3 = (r'%s'%(sp[0] + '.mp3'))
    video = VideoFileClip(m4);
    audio = video.audio
    audio.write_audiofile(m3)
    audio.close()
    video.close()
    return True;




