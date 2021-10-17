import pytube
from pytube import YouTube

t = 0
while not t > 0:
    link_input = input("Please enter the YouTube video URL you are looking to download: ")
    try:
        yt = YouTube(link_input)
        print('URL valid! Proceeding further.')
        yt.streams.filter(progressive=True, type='video', file_extension='mp4').order_by('resolution')[-1].download(
            '/home/ravik/Downloads/staging')
        print("Video downloaded to default downloads location")
        t += 1
    except pytube.exceptions.RegexMatchError:
        print("URL is not correct and program cannot find a match video!")
    except:
        print("Unknown error occurred")

print("Program completed!")
