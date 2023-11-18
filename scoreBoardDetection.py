import os
import cv2
import numpy as np

class scoreBoardDetection:

    def process_frames(self,input_folder, output_folder):
        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Iterate over frames in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                frame_path = os.path.join(input_folder, filename)

                # Read the frame
                frame = cv2.imread(frame_path)

                # Detect scoreboard in the frame
                def detect_scoreboard(frame):
                    # net = cv2.dnn.readNet("yolov7.pt", "yolov7.cfg") 
                    net = cv2.dnn.readNet("C:/BE/project_implementation/yolov7.pt", "C:/Users/omkar/YOLO7/yolov7/cfg") 
                    layer_names = net.getLayerNames()
                    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

                    # Resize and convert the image to blob format
                    height, width, channels = frame.shape
                    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
                    net.setInput(blob)
                    outs = net.forward(output_layers)

                    # Extract information from YOLO output
                    class_ids = []
                    confidences = []
                    boxes = []

                    for out in outs:
                        for detection in out:
                            scores = detection[5:]
                            class_id = np.argmax(scores)
                            confidence = scores[class_id]
                            if confidence > 0.5 and class_id == 0:  # Assuming scoreboard class is 0
                                # Object detected
                                center_x = int(detection[0] * width)
                                center_y = int(detection[1] * height)
                                w = int(detection[2] * width)
                                h = int(detection[3] * height)

                                # Rectangle coordinates
                                x = int(center_x - w / 2)
                                y = int(center_y - h / 2)

                                boxes.append([x, y, w, h])
                                confidences.append(float(confidence))
                                class_ids.append(class_id)

                    return boxes

                scoreboard_boxes = detect_scoreboard(frame)

                # If a scoreboard is detected, create a new folder and save the frame
                if scoreboard_boxes:
                    new_folder = os.path.join(output_folder, "scoreboard_frames")
                    if not os.path.exists(new_folder):
                        os.makedirs(new_folder)

                    # Save the frame in the new folder
                    cv2.imwrite(os.path.join(new_folder, filename), frame)

   