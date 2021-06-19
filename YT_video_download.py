from pytube import YouTube
link = input("Enter link: ")
video = YouTube(link)
stream = video.streams.get_by_resolution("1080p")
print("Download inprogress...")
stream.download()
print("Download complete")



