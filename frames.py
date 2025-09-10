import cv2
import os

video_folder = "colorization_dataset/videos"
frames_folder = "colorization_dataset/frames"
os.makedirs(frames_folder, exist_ok=True)

for video_file in os.listdir(video_folder):
    if video_file.endswith(".mp4"):
        cap = cv2.VideoCapture(os.path.join(video_folder, video_file))
        count = 0
        video_name = os.path.splitext(video_file)[0]
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imwrite(f"{frames_folder}/{video_name}_frame{count:04d}.jpg", frame)
            count += 1
        cap.release()
