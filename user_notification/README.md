# Django Notification System

A Django application for booking appointments with email and SMS notifications.

## Features

- ✅ Appointment booking system
- ✅ User notifications dashboard
- ✅ Email notifications via Gmail SMTP
- ✅ SMS notifications via Twilio
- ✅ SQLite database
- ✅ Responsive web interface

## Setup Instructions

### 1. Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### 2. API Configuration

#### Gmail Setup (Email)
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Enable 2-Factor Authentication
3. Generate an App Password:
   - Go to Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Use this 16-character password (ignore spaces)

#### Twilio Setup (SMS)
1. Create account at [Twilio](https://www.twilio.com/)
2. Get your Account SID and Auth Token from Dashboard
3. Purchase a phone number for SMS sending
4. Verify your phone number for testing

### 3. Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env` with your actual credentials:
```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=+1234567890
```

### 4. Django Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### 5. Access the Application

- **Appointment Booking**: http://127.0.0.1:8000/appointment/
- **Notifications**: http://127.0.0.1:8000/notifications/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## API Integration Details

### Email Notifications
- Uses Gmail SMTP with app passwords
- Automatic confirmation emails on appointment booking
- Error handling with logging

### SMS Notifications
- Uses Twilio REST API
- Automatic SMS confirmations on appointment booking
- International number support
- Delivery status tracking

## Testing

### Test Email
```python
from normal_messages.utils import send_email_notification
send_email_notification("Test Subject", "Test Message", "recipient@example.com")
```

### Test SMS
```python
from normal_messages.utils import send_sms_notification
send_sms_notification("Test SMS", "+1234567890")
```

## Security Notes

- Never commit `.env` file to version control
- Use app passwords for Gmail, not regular passwords
- Keep Twilio credentials secure
- Use environment variables for all sensitive data

## Troubleshooting

### Email Issues
- Verify Gmail app password is correct
- Check Gmail security settings
- Ensure less secure apps are allowed (or use app passwords)

### SMS Issues
- Verify Twilio credentials
- Check phone number format (+country code)
- Ensure sufficient Twilio balance
- Check Twilio logs in dashboard

## Cost Information

- **Gmail**: Free (with app passwords)
- **Twilio SMS**: ~$0.0075 per message (US), varies by country
- **Twilio Phone Number**: ~$1/month

## Alternative Services

### Email Alternatives
- SendGrid, Mailgun, Amazon SES
- More reliable than Gmail for production

### SMS Alternatives
- AWS SNS, Nexmo (Vonage), MessageBird
- Different pricing and features