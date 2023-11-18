import re
from framesExtraction import framesExtraction
from textExtraction import textExtraction
# from scoreBoardDetection import scoreBoardDetection


def main():
    print("Enter the video path : ")
    video_path = input()
    print("\n")

    print("Enter the frames storage path : ")
    frames_path = input()

    frames_ext = framesExtraction()
    text_ext = textExtraction()
    # score_board_detect = scoreBoardDetection()

    frames_ext.extract_frames(video_path, frames_path)
    get_text = text_ext.extract_text(
        "C:/BE/project_implementation/frames_directory", "frames_dataset.txt")

    # # Open the file containing the text
    with open("frames_dataset2.txt", 'r') as file:
        file_content = file.read()

    # # Define a regular expression pattern to match the text "336-6"
    pattern = r'(PAK) \(\d+-\d+)'

    # # Use re.findall to find all matches in the text
    matches = re.findall(pattern, file_content)

    # # Print the matches
    for match in matches:
        print(match)

    # print("path_to_input_folder")  # Replace with the path to your input frames folder
    # input_folder_path = input()
    # print("path_to_output_folder")  # Replace with the path to your output frames folder
    # output_folder_path = input()

    # score_board_detect.process_frames(input_folder_path, output_folder_path)


if __name__ == "__main__":

    main()

