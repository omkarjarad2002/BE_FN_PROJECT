import cv2
import os
import pytesseract
import csv
import re


class textExtraction:
    def __init__(self):
        pass

    def extract_text(self, frames_folder_path, extracted_text_path):

        # Initialize the CSV writer
        with open(extracted_text_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Frame', 'Runs', 'Wickets', 'Team Name'])

        # Iterate through frames
        for frame_filename in os.listdir(frames_folder_path):
            if frame_filename.endswith('.jpg'):
                frame_path = os.path.join(frames_folder_path, frame_filename)
                frame = cv2.imread(frame_path)

                scorecard_text = pytesseract.image_to_string(frame)

                # Extract runs, wickets, and team name using regular expressions
                runs_match = re.search(
                    r'(\d+)-(\d+)\s+NEED\s+(\d+)\s+TO WIN', scorecard_text)
                wickets_match = re.search(r'(\d+)\s+wickets', scorecard_text)
                team_name_match = re.search(
                    r'(\w+)\s+\(\d+-\d+', scorecard_text)

                # Initialize variables with default values
                runs = "N/A"
                wickets = "N/A"
                team_name = "N/A"

                # Update variables if matches are found
                if runs_match:
                    # Format runs as "336-6"
                    runs = f"{runs_match.group(1)}-{runs_match.group(2)}"
                if wickets_match:
                    wickets = wickets_match.group(1)
                if team_name_match:
                    team_name = team_name_match.group(1)
                # Append the results to the CSV file
                with open(extracted_text_path, 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(
                        # [frame_filename, runs, wickets, team_name]
                        [scorecard_text]
                    )
