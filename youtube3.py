from pytube import YouTube
from pytube.cli import on_progress
import os


def describe(self):
    print(f"The title of this video is {self.title}")
    print(f"This video has {self.views} views")
    print(f"Video has {self.rating} rating")
    print(f"The available streams are {self.streams.filter(progressive= True)}")


link = input("Enter the link you want to download")
path = r"C:\Users\acer\Downloads"
os.chdir(path)
yt = YouTube(link, on_progress_callback=on_progress)
ys1 = yt.streams.get_highest_resolution()
ys1.download()
describe(yt)
