from pytube import YouTube
import os 
import sys
from threading import Thread
from time import sleep
import requests # request img from web
import shutil # save img locally
def url_list ():
  number_of_urls = int(input("how many urls do you have: "))
  count = 1
  i = 1
  urls = []
  while i<=number_of_urls:
    url = input (f"url[{count}]: ")
    urls.append(url)
    count+=1
  return urls

def videoDownloader (urls,itag):
  for i in urls:
    yt = YouTube(i)
    print (f"downloading...[{yt.title}]")
    yt.streams.get_by_itag(itag).download()
    print ("done...")

def songDownloader (urls):
  for i in urls:
    yt = YouTube(i)
    print ("downloading...")
    yt.streams.get_by_itag(251).download()
    print (f"downloaded :[{yt.title}]")
    print ("converting to mp3")
    os.system(f"ffmpeg -i '{yt.title}.webm' '{yt.title}.mp3")
    print ("converting done ...")

'''
# YouTube video downloader in normal way
try :
  if sys.argv[1] == "-v":
    urls = url_list()
    try :
      videoDownloader(urls,sys.argv[2])
    except IndexError:
        print ("itag is not given")
  elif sys.argv[1] == "-s":
    urls = url_list()
    songDownloader(urls)
except IndexError:
  print ("argument is not given, give -v <itag> for video and -s of song ")
'''
# YouTube video downloader in multithreading way

song_titles = []



class ytDownloader:
  def imageDownloader (self,url,file_name):
    #url = input('Please enter an image URL (string):') #prompt user for img url
    #file_name = input('Save image as (string):') #prompt user for file_name
    
    res = requests.get(url, stream = True)
    
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        #print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')
    
  def videoDownloader (self,url,itag):
    yt = YouTube(url)
    print ("downloading..")
    yt.streams.get_by_itag(itag).download()
    print (f"done download [{yt.title}]")


# song downloader
  def conver_to_mp3 (title):
    print ("converting to mp3")
    os.system(f"ffmpeg -i '{title}.webm' '{title}.mp3")
    
    os.system(f"`ffmpeg -i '{title}.mp3' -i '{title}.png' -c copy -map 0 -map 1 '{title}.mp3'")
    print ("converting done ...")

  def songDownloader (self,url,itag):
    yt = YouTube(url)
    print ("downloading..")
    #yt.streams.get_by_itag(itag).download()
    img = self.imageDownloader(yt.thumbnail_url,f"{yt.title}.png")
    song_titles.append(yt.title)
    print (f"done download [{yt.title}]")
    return f"done download [{yt.title}]"
  def main ():
    pass


def audio_downloader (itag):
  number_of_urls = int(input("how many urls do you have: "))
  balance_url = []
  count = 1
  i = 1
  while i<=number_of_urls:
    url = input(f"url [{i}]:")
    yt = ytDownloader()
    if i<=3:
      thread = Thread(target=yt.songDownloader,args=(url,itag))
      thread.start()
    else:
      balance_url.append(url)

def video_downloader (itag):
  number_of_urls = int(input("how many urls do you have: "))
  balance_url = []
  count = 1
  i = 0
  threads = []
  while i<number_of_urls:
    url = input(f"url [{count}]:")
    yt = ytDownloader()
    if i<=3:
      threads[i] = Thread(target=yt.videoDownloader,args=(url,itag))
      thread[i].start()
    else:
      balance_url.append(url)
    i+=1
    count+=1
  for i in threads:
    

if sys.argv[1] == "-v":
  if sys.argv[2] != "":
    video_downloader(sys.argv[2])
  else:
    video_downloader(18)
elif sys.argv[1] == "-s":
  if sys.argv[2] != "":
    audio_downloader(sys.argv[2])
  else:
    audio_downloader(251)
else :
  print ("argument is not valid ")

print (song_titles)