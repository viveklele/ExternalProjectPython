from pytube import YouTube
link = input("Enter link: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
print("Download inprogress...")
stream.download()
print("Download complete")



