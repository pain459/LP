import requests
import threading

def download_file(url, filename):
    # Function to download a file from a given URL
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

def main():
    url = input("Enter the URL of the file to download: ")
    filename = input("Enter the filename to save as: ")

    # Number of threads to use for downloading
    num_threads = int(input("Enter the number of threads to use: "))

    # Calculate the range for each thread
    thread_ranges = [(i * (int(requests.head(url).headers.get('Content-Length')) // num_threads),
                      (i + 1) * (int(requests.head(url).headers.get('Content-Length')) // num_threads) - 1)
                     for i in range(num_threads)]

    # Create and start threads
    threads = []
    for i in range(num_threads):
        start, end = thread_ranges[i]
        t = threading.Thread(target=download_file, args=(url, f"{filename}_part_{i}", start, end))
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Merge downloaded parts into a single file
    with open(filename, 'wb') as f:
        for i in range(num_threads):
            with open(f"{filename}_part_{i}", 'rb') as part:
                f.write(part.read())

    print("Download complete!")

if __name__ == "__main__":
    main()
