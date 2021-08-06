from pytube import YouTube
YouTube_link = input("Enter the link")
my_video = YouTube(YouTube_link)
print("downloading...") #not must in program i have written so that when run program looks cool, as it shows file is downloading
my_video = my_video.streams.get_highest_resolution()
# automatically download video in highest resolution
my_video.download()
print("video downloaded successfully")
