from __future__ import unicode_literals

from pafys import pafy
import youtube_dl
import os
import sys


'''

>python3 ytdl.py download [path to videos folder  eg. /Desktop/videos/] [video url]

   > downloads video from video url to videos folder

>python3 ytdl.py delete [path to videos folder  eg. /Desktop/videos]

   > deletes all videos in videos folder

'''


class ytdl:

  def __init__(self,path_to_videos_folder=None,video_url=None):
    self.path_to_videos = path_to_videos_folder
    self.video_url = video_url


  def downloader(self):

    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',       
        'outtmpl': f'{self.path_to_videos}%(title)s',
        'noplaylist' : True,        
        'progress_hooks': [my_hook],  
    }
    vid = pafy.new(self.video_url)
    vidt = vid.title

    if f"{vidt}.mp4" not in os.listdir(self.path_to_videos):
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([self.video_url])

    os.rename(os.path.join(self.path_to_videos,vidt),str(os.path.join(self.path_to_videos,vidt + ".mp4")))
    return (os.path.join(self.path_to_videos,vidt))

  def deleter(self):
    for filename in os.listdir(self.path_to_videos):
      os.remove(os.path.join(self.path_to_videos,filename))

ytdl1 = ytdl(path_to_videos_folder=sys.argv[2],video_url=sys.argv[3])



if sys.argv[1] == "download":
  ytdl1.downloader()
elif sys.argv[1] == "delete":
  ytdl1.deleter()
