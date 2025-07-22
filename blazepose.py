import torch
import numpy as np
import cv2
from blazepose_landmark import BlazePoseLandmark
from blazepose_detection import BlazePoseDetection
from blazepose_renderer import BlazePoseRenderer

class BlazePose:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.detector = BlazePoseDetection().to(self.device).eval()
        self.landmark_model = BlazePoseLandmark().to(self.device).eval()

    def process_frame(self, frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_tensor = torch.tensor(image_rgb / 255.0, dtype=torch.float32).permute(2, 0, 1).unsqueeze(0).to(self.device)

        with torch.no_grad():
            detections = self.detector(image_tensor)
            if detections is None or len(detections) == 0:
                return None

            keypoints = self.landmark_model(image_tensor, detections)
            if keypoints is None:
                return None

        # Extract meaningful points
        landmarks = keypoints[0]  # (33, 3)
        pose_dict = {
            "right_shoulder": landmarks[12].tolist(),
            "right_hip": landmarks[24].tolist(),
            "right_knee": landmarks[26].tolist(),
            "right_ankle": landmarks[28].tolist(),
            "head": landmarks[0].tolist()
        }

        return pose_dict
