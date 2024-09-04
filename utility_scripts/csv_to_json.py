import csv
import json
import os

class CSVtoJSONConverter:
    def __init__(self, source_dir, dest_dir):
        """
        Initialize the converter with the source directory containing CSV files
        and the destination directory where JSON files will be saved.
        """
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
    
    def convert_file(self, csv_file, json_file):
        """
        Convert a single CSV file to JSON.
        """
        with open(csv_file, mode='r', encoding='utf-8-sig') as file:
            csv_reader = csv.DictReader(file)
            rows = list(csv_reader)
        
        with open(json_file, mode='w', encoding='utf-8') as file:
            json.dump(rows, file, indent=4)
        
        print(f"Converted {csv_file} to {json_file}")

    def convert_all(self):
        """
        Convert all CSV files in the source directory to JSON format.
        """
        for filename in os.listdir(self.source_dir):
            if filename.endswith('.csv'):
                csv_file = os.path.join(self.source_dir, filename)
                json_file = os.path.join(self.dest_dir, filename.replace('.csv', '.json'))
                self.convert_file(csv_file, json_file)
    
    def list_csv_files(self):
        """
        List all CSV files in the source directory.
        """
        csv_files = [file for file in os.listdir(self.source_dir) if file.endswith('.csv')]
        return csv_files


# Example usage
if __name__ == "__main__":
    source_directory = "/home/ravik/src_git/LP/utility_scripts/"
    destination_directory = "/home/ravik/src_git/LP/utility_scripts/"
    
    converter = CSVtoJSONConverter(source_directory, destination_directory)

    # List CSV files in the source directory
    csv_files = converter.list_csv_files()
    print(f"CSV files found: {csv_files}")
    
    # Convert all CSV files in the source directory to JSON
    converter.convert_all()
