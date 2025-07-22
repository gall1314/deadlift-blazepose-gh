import cv2

class BlazePoseRenderer:
    def __init__(self):
        pass

    def render(self, frame, landmarks: dict):
        # ציור נקודות פשוט על התמונה
        for name, coord in landmarks.items():
            x, y, z = coord
            cv2.circle(frame, (int(x), int(y)), radius=5, color=(0,255,0), thickness=-1)
        return frame
