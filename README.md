# you-tube-downloader
# Abhishek Upadhyay
from pytube import YouTube
YouTube_link = input("Enter the link")
my_video = YouTube(YouTube_link)
print("downloading...")
# my_video = my_video.streams.get_highest_resolution
# my_video.download()
my_video = my_video.streams.get_highest_resolution()

#or
#my_video = my_video.streams.first()

#Download video
my_video.download()
print("video downloaded successfully")
