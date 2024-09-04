import time
import os

class LogFileMonitor:
    def __init__(self, file_path, keyword=None):
        """
        Initialize the monitor with the file path and an optional keyword to monitor.
        - file_path: Path to the log file.
        - keyword: Keyword or pattern to search for.
        """
        self.file_path = file_path
        self.keyword = keyword

    def follow(self):
        """
        Follow the log file in real-time and print new lines as they are added.
        If a keyword is specified, only lines containing the keyword will be printed.
        """
        with open(self.file_path, 'r') as file:
            # Move to the end of the file
            file.seek(0, os.SEEK_END)

            while True:
                line = file.readline()
                if not line:
                    time.sleep(1)  # Sleep briefly and wait for new lines
                    continue
                
                if self.keyword:
                    if self.keyword in line:
                        print(f"[ALERT] {line.strip()}")
                else:
                    print(line.strip())

    def start(self):
        """
        Start monitoring the log file.
        """
        print(f"Monitoring {self.file_path} for changes...")
        if self.keyword:
            print(f"Filtering logs with keyword: '{self.keyword}'")
        self.follow()

# Example usage
if __name__ == "__main__":
    log_file_path = "/home/ravik/src_git/LP/utility_scripts/sample_log_file.log"  # Specify the log file path
    keyword_to_watch = "ERROR"  # Specify the keyword to look for (optional)

    monitor = LogFileMonitor(log_file_path, keyword_to_watch)
    
    # Start monitoring the log file for the specified keyword
    monitor.start()
