import torch
import torch.nn as nn

# דוגמה: רשת פשוטה להדגמת שימוש
class BlazePoseDetection(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Flatten()
        )

    def forward(self, x):
        # return dummy detection: مربع מלא
        batch_size = x.shape[0]
        return torch.ones((batch_size, 1, 4))  # x, y, w, h
