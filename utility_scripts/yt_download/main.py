from pytube import YouTube
from pytube.streams import Stream
from typing import Optional

def download_video(url: str, resolution: str = '720p') -> None:
    try:
        # Create a YouTube object with the URL
        yt: YouTube = YouTube(url)
        
        # Get the highest resolution stream available
        stream: Optional[Stream] = yt.streams.filter(res=resolution).first()
        
        if not stream:
            print(f"No stream available with resolution {resolution}. Downloading highest available resolution.")
            stream = yt.streams.get_highest_resolution()
        
        if stream:
            # Download the video
            stream.download()
            print(f"Video downloaded successfully: {yt.title}")
        else:
            print("No streams available to download.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'https://www.youtube.com/watch?v=M_K3T0Bdnv0'  # Replace with your desired YouTube video URL
download_video(url, '720p')
