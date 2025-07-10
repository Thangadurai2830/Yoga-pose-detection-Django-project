# poseapp/pose_detection/detector.py

import cv2
import mediapipe as mp
import os
from .utils import draw_landmarks, save_annotated_image, get_pose_label_and_feedback

mp_pose = mp.solutions.pose

def classify_pose(landmarks):
    """
    Rule-based classification using pose landmark coordinates (very basic logic).
    Replace with ML model for better accuracy.
    """
    left_shoulder = landmarks.landmark[11].y
    right_shoulder = landmarks.landmark[12].y
    left_hip = landmarks.landmark[23].y
    right_hip = landmarks.landmark[24].y
    left_knee = landmarks.landmark[25].y
    right_knee = landmarks.landmark[26].y
    left_ankle = landmarks.landmark[27].y
    right_ankle = landmarks.landmark[28].y

    # Heuristic-based classification (simplified rules for demo purposes)
    if left_ankle < left_knee and right_ankle > right_knee:
        return "Tree Pose"
    elif abs(left_hip - right_hip) < 0.05 and abs(left_knee - right_knee) > 0.2:
        return "Warrior Pose"
    elif abs(left_knee - right_knee) < 0.05 and left_knee > left_hip:
        return "Chair Pose"
    elif left_hip < left_knee and left_ankle > left_knee:
        return "Downward Dog"
    elif left_shoulder > left_hip and left_hip > left_knee:
        return "Cobra"
    elif abs(left_shoulder - right_shoulder) < 0.03 and left_ankle > left_knee:
        return "Mountain Pose"
    elif left_ankle < left_knee and left_knee < left_hip:
        return "Shoulder Stand"
    elif abs(left_hip - right_hip) < 0.05 and abs(left_ankle - right_ankle) < 0.05:
        return "Triangle"
    else:
        return "Unknown Pose"

def detect_pose(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return 'Pose Not Found', 'Unable to read the image.', '/static/assets/no-pose.png'

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_pose.Pose(static_image_mode=True) as pose:
        results = pose.process(image_rgb)

        if not results.pose_landmarks:
            return 'No Pose', 'Pose not detected. Please try again.', '/static/assets/no-pose.png'

        detected_pose = classify_pose(results.pose_landmarks)
        annotated_image = draw_landmarks(image.copy(), results.pose_landmarks)
        annotated_image_path = save_annotated_image(annotated_image)
        pose_label, feedback = get_pose_label_and_feedback(detected_pose)

        return pose_label, feedback, annotated_image_path
