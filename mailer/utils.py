from django.core.mail import send_mail
from django.conf import settings

def send_pose_feedback_email(to_email, pose_name, feedback):
    subject = f"Your Yoga Pose Result: {pose_name}"
    message = f"""
Hello,

Here are the results of your recent yoga pose detection:

🧘 Pose Name: {pose_name}
📝 Feedback: {feedback}

Thank you for using our Yoga Pose Detection System!
Stay healthy and flexible! 💪🧘‍♀️

— YogaPose AI Team
    """
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [to_email],
        fail_silently=False,
    )
