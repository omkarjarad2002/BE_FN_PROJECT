import cv2
import os


class framesExtraction:

    def __init__(self):
        pass

    def extract_frames(self, video_path, frames_path):

        # Create the output directory if it doesn't exist
        if not os.path.exists(frames_path):
            os.makedirs(frames_path)

        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Initialize frame counter
        frame_count = 0

        # Loop through the video frames
        while True:
            ret, frame = cap.read()

            # Break the loop if we have reached the end of the video
            if not ret:
                break

            # Save the frame as an image
            frame_filename = os.path.join(
                frames_path, f'frame_{frame_count:04d}.jpg')
            cv2.imwrite(frame_filename, frame)

            frame_count += 1

        # Release the video capture object
        cap.release()

        # Print the number of frames saved
        print(f'{frame_count} frames saved.')

        # Close all OpenCV windows (if any)
        cv2.destroyAllWindows()
