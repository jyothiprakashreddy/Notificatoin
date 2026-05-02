#!/usr/bin/env python
"""
Test script for notification functions
Run this to test email and SMS functionality
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_notification.settings')
django.setup()

from normal_messages.utils import send_email_notification, send_sms_notification

def test_notifications():
    print("🧪 Testing Notification System")
    print("=" * 50)

    # Test data
    test_email = "test@example.com"
    test_phone = "+1234567890"
    test_message = "This is a test notification from Django Notification System"

    print("📧 Testing Email Notification...")
    print(f"To: {test_email}")
    print(f"Message: {test_message}")

    # Note: This will fail without proper credentials, but shows the integration
    email_result = send_email_notification("Test Subject", test_message, test_email)
    print(f"Email Result: {'✅ Success' if email_result else '❌ Failed'}")

    print("\n📱 Testing SMS Notification...")
    print(f"To: {test_phone}")
    print(f"Message: {test_message}")

    sms_result = send_sms_notification(test_message, test_phone)
    print(f"SMS Result: {'✅ Success' if sms_result else '❌ Failed'}")

    print("\n" + "=" * 50)
    print("📝 Setup Instructions:")
    print("1. Configure Gmail app password in settings.py")
    print("2. Set up Twilio account and add credentials")
    print("3. Update .env file with real credentials")
    print("4. Test again with: python test_notifications.py")

if __name__ == "__main__":
    test_notifications()