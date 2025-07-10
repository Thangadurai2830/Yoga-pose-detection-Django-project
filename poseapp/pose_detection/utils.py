# poseapp/pose_detection/utils.py

import cv2
import os
from datetime import datetime
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def draw_landmarks(image, landmarks):
    mp_drawing.draw_landmarks(
        image,
        landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
        connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
    )
    return image

def save_annotated_image(image, directory='static/assets'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = f"pose_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    path = os.path.join(directory, filename)
    cv2.imwrite(path, image)
    return '/' + path.replace('\\', '/')

def get_pose_label_and_feedback(pose_name):
    pose_labels = {
        'Tree Pose': 'Tree Pose 🌳',
        'Warrior Pose': 'Warrior Pose ⚔️',
        'Chair Pose': 'Chair Pose 🪑',
        'Downward Dog': 'Downward Dog 🐶',
        'Cobra': 'Cobra Pose 🐍',
        'Mountain Pose': 'Mountain Pose ⛰️',
        'Shoulder Stand': 'Shoulder Stand 🧍‍♂️',
        'Triangle': 'Triangle Pose 🔺',
        'Unknown Pose': 'Unknown Pose ❓',
        'No Pose': 'No Pose 🚫'
    }

    feedback_messages = {
        'Tree Pose': 'Great balance and posture! Keep your back straight. 🙏',
        'Warrior Pose': 'Strong and focused. Maintain your core engaged! 💪',
        'Chair Pose': 'Nice squat! Ensure knees don’t cross your toes. 🧘‍♂️',
        'Downward Dog': 'Relax your spine and press your heels down. 🐾',
        'Cobra': 'Keep your chest lifted and shoulders relaxed. 🐍',
        'Mountain Pose': 'Simple yet powerful. Stand tall and grounded. 🌟',
        'Shoulder Stand': 'Maintain alignment and support your back. 🤸',
        'Triangle': 'Reach out and lengthen both sides of your body. 🔺',
        'Unknown Pose': 'Unclear pose. Please try again or adjust your posture.',
        'No Pose': 'No person detected. Try again in better lighting.'
    }

    return (
        pose_labels.get(pose_name, 'Unknown Pose ❓'),
        feedback_messages.get(pose_name, 'Keep practicing regularly! 💡')
    )
