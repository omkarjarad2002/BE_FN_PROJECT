from file1 import framesExtraction
from file2 import textExtraction


def main():
    print("Enter the video path : ")
    video_path = input()
    print("\n")

    print("Enter the frames storage path : ")
    frames_path = input()

    frames_ext = framesExtraction()
    text_ext = textExtraction()

    frames_ext.extract_frames(video_path, frames_path)
    text_ext.extract_text(
        "C:/BE/project_implementation/frames_directory", "frames_dataset2.csv")


if __name__ == "__main__":

    main()
