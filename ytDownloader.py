from pytube import YouTube
import os 
import sys
from threading import Thread
from time import sleep

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

# YouTube video downloader in multithreading way
class ytDownloader:
  def videoDownloader ():
    pass
  def songDownloader ():
    pass
  def main ():
    pass
    