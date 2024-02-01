import speedtest

wifi = speedtest.Speedtest()

download_speed = wifi.download(threads=4)
upload_speed = wifi.upload(threads=4)
print(f"Your download speed is {download_speed/1024/1024/8} MBps.")
print(f"Your upload speed is {upload_speed/1024/1024/8} MBps.")
