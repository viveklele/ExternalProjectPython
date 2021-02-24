from pytube import YouTube
save_path = 'D:\Vivek\PythonProjects\ExternalProjects'
link = 'https://youtu.be/eIc4mqyN1Q8?list=RDMsl2fl3h59I'

try:
    yt = YouTube(link)
except:
    print('Error connection')


mp4file = yt.filter('mp4')
yt.set_filename('Falling')
d_video = yt.get(mp4file[-1].extention, mp4file[-1].resolution)
try:
    d_video.downlode(save_path)
except:
    print('some error')
print('downlode complete')