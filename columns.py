import os
import pandas as pd

def main():
    directory_path = './uploads'

    # Checks for any CSV file in the directory
    csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

    # Check if exactly one CSV file is found
    if len(csv_files) != 0:
        csv_file = csv_files[0]
        csv_file_path = os.path.join(directory_path, csv_file)

        if os.path.isfile(csv_file_path):
            df = pd.read_csv(csv_file_path)
            for column_name in df.columns:
                    print(f"{column_name}")
        else:
            print(f"Invalid file format. File '{csv_file}' is not a CSV file.")
    else:
        return
        
main()