from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Notification
from .utils import send_appointment_notifications
from datetime import datetime


def user_notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user)
    else:
        notifications = Notification.objects.none()  # Return empty queryset for unauthenticated users
    return render(request, 'notifications.html', {'notifications': notifications})


def appointment_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        appointment_date_str = request.POST.get('appointment_date')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Parse the date
        appointment_date = None
        if appointment_date_str:
            appointment_date = datetime.strptime(appointment_date_str, '%Y-%m-%d').date()

        # Create message with formatted date
        date_str = appointment_date.strftime('%B %d, %Y') if appointment_date else 'TBD'
        message = f"Hello {name}, your appointment is booked on {date_str}"

        # Create notification in database
        Notification.objects.create(
            user=request.user if request.user.is_authenticated else None,
            name=name,
            appointment_day=date_str,  # Keep for backward compatibility
            appointment_date=appointment_date,  # New date field
            phone=phone,
            email=email,
            message=message
        )

        # Send real notifications
        notification_results = send_appointment_notifications(name, appointment_date, phone, email)

        # Prepare success message
        success_msg = "Appointment booked successfully!"
        if notification_results['email_sent']:
            success_msg += " Email confirmation sent."
        if notification_results['sms_sent']:
            success_msg += " SMS confirmation sent."

        return render(request, 'appointment.html', {'msg': success_msg})

    return render(request, 'appointment.html')
