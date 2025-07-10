# mailer/views.py
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings

@csrf_exempt
def send_mail_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        # === 1. Email to admin ===
        subject = f"New Contact from {name}"
        admin_message = f"""
        📬 New Contact Form Submission

        🧑 Name: {name}
        📧 Email: {email}
        📱 Mobile: {mobile}

        📝 Message:
        {message}
        """

        send_mail(
            subject,
            admin_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],  # Make sure this is defined in settings.py
            fail_silently=False,
        )

        # === 2. Confirmation email to user ===
        user_subject = "🧘 Thanks for Contacting YogaPoseAI!"
        user_message = f"""
        Hello {name},

        Thank you for reaching out to us. 🙏
        We’ve received your message and will get back to you soon!

        Your Message:
        {message}

        Stay balanced,
        Team YogaPoseAI 🧘‍♀️
        """

        send_mail(
            user_subject,
            user_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],  # Sending to user
            fail_silently=False,
        )

        return redirect('/')  # Or show a "thank you" page
    return HttpResponse("Invalid Request", status=400)
