from pytube import YouTube

enter_link = input('enter YouTube link: ')

streme = YouTube(enter_link, ).streams.get_highest_resolution()

print('downloading...')

streme.download()

print('download complete')