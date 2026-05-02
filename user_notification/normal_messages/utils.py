from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
import logging

logger = logging.getLogger(__name__)

def send_email_notification(subject, message, recipient_email):
    """
    Send email notification using Django's email backend
    """
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient_email],
            fail_silently=False,
        )
        logger.info(f"Email sent successfully to {recipient_email}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email to {recipient_email}: {str(e)}")
        return False

def send_sms_notification(message, recipient_phone):
    """
    Send SMS notification using Twilio
    """
    try:
        # Initialize Twilio client
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Send SMS
        message = client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=recipient_phone
        )

        logger.info(f"SMS sent successfully to {recipient_phone}, SID: {message.sid}")
        return True
    except Exception as e:
        logger.error(f"Failed to send SMS to {recipient_phone}: {str(e)}")
        return False

def send_appointment_notifications(name, appointment_date, phone, email):
    """
    Send both email and SMS notifications for appointment booking
    """
    subject = "Appointment Confirmation"
    date_str = appointment_date.strftime('%B %d, %Y') if appointment_date else 'TBD'
    message = f"Hello {name}, your appointment is booked on {date_str}"

    email_sent = False
    sms_sent = False

    # Send email if email address is provided
    if email:
        email_sent = send_email_notification(subject, message, email)

    # Send SMS if phone number is provided
    if phone:
        sms_sent = send_sms_notification(message, phone)

    return {
        'email_sent': email_sent,
        'sms_sent': sms_sent
    }