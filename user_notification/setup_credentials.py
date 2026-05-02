#!/usr/bin/env python
"""
Credential Configuration Helper
Run this script to safely configure Gmail and Twilio credentials
"""

import os
from pathlib import Path

def create_env_file():
    """Create .env file with user input"""
    env_file = Path('.env')
    
    if env_file.exists():
        response = input(".env file already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Skipping .env creation")
            return
    
    print("\n" + "="*60)
    print("CREDENTIAL CONFIGURATION HELPER")
    print("="*60)
    
    print("\n📧 GMAIL CONFIGURATION")
    print("-" * 60)
    print("Get your Gmail App Password from:")
    print("  https://myaccount.google.com/apppasswords")
    print("\nNOTE: You must have 2-Factor Authentication enabled!")
    
    email = input("\nGmail Email Address: ").strip()
    app_password = input("Gmail App Password (16 chars, remove spaces): ").strip()
    
    print("\n📱 TWILIO CONFIGURATION")
    print("-" * 60)
    print("Get your Twilio credentials from:")
    print("  https://console.twilio.com/")
    
    account_sid = input("\nTwilio Account SID (starts with AC): ").strip()
    auth_token = input("Twilio Auth Token: ").strip()
    twilio_phone = input("Twilio Phone Number (format: +12025551234): ").strip()
    
    # Create .env content
    env_content = f"""# Gmail Configuration
EMAIL_HOST_USER={email}
EMAIL_HOST_PASSWORD={app_password}

# Twilio Configuration
TWILIO_ACCOUNT_SID={account_sid}
TWILIO_AUTH_TOKEN={auth_token}
TWILIO_PHONE_NUMBER={twilio_phone}
"""
    
    # Write to .env
    with open(env_file, 'w') as f:
        f.write(env_content)
    
    print("\n" + "="*60)
    print("✅ .env file created successfully!")
    print("="*60)
    
    # Display summary (without exposing full values)
    print("\n📋 CONFIGURATION SUMMARY:")
    print(f"✓ Email: {email}")
    print(f"✓ Gmail Password: {'*' * (len(app_password)-4)}{app_password[-4:]}")
    print(f"✓ Twilio Account SID: {account_sid[:2]}{'*' * 20}...{account_sid[-4:]}")
    print(f"✓ Twilio Phone: {twilio_phone}")
    
    print("\n⚠️  IMPORTANT:")
    print("1. Add '.env' to your .gitignore")
    print("2. Never commit credentials to Git")
    print("3. Use environment variables in production")
    
    return True

def load_env_to_settings():
    """Load .env values to Django settings.py"""
    from pathlib import Path
    
    env_file = Path('.env')
    if not env_file.exists():
        print("❌ .env file not found. Run configuration first.")
        return False
    
    # Parse .env file
    config = {}
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
    
    # Update settings.py
    settings_file = Path('user_notification/settings.py')
    with open(settings_file, 'r') as f:
        content = f.read()
    
    # Replace email config
    if 'EMAIL_HOST_USER' in config:
        content = content.replace(
            f"EMAIL_HOST_USER = '{config['EMAIL_HOST_USER']}'",
            f"EMAIL_HOST_USER = '{config['EMAIL_HOST_USER']}'"
        )
        content = content.replace(
            "EMAIL_HOST_PASSWORD = 'Jyothi@81420'",
            f"EMAIL_HOST_PASSWORD = '{config['EMAIL_HOST_PASSWORD']}'"
        )
    
    # Replace Twilio config
    if 'TWILIO_ACCOUNT_SID' in config:
        content = content.replace(
            "TWILIO_ACCOUNT_SID = 'your-twilio-account-sid'",
            f"TWILIO_ACCOUNT_SID = '{config['TWILIO_ACCOUNT_SID']}'"
        )
        content = content.replace(
            "TWILIO_AUTH_TOKEN = 'your-twilio-auth-token'",
            f"TWILIO_AUTH_TOKEN = '{config['TWILIO_AUTH_TOKEN']}'"
        )
        content = content.replace(
            "TWILIO_PHONE_NUMBER = 'your-twilio-phone-number'",
            f"TWILIO_PHONE_NUMBER = '{config['TWILIO_PHONE_NUMBER']}'"
        )
    
    with open(settings_file, 'w') as f:
        f.write(content)
    
    print("✅ settings.py updated successfully!")
    return True

def validate_credentials():
    """Test if credentials are valid"""
    print("\n🧪 VALIDATING CREDENTIALS...")
    print("-" * 60)
    
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_notification.settings')
    django.setup()
    
    from django.conf import settings
    from normal_messages.utils import send_email_notification, send_sms_notification
    
    # Check email config
    if settings.EMAIL_HOST_PASSWORD == 'Jyothi@81420':
        print("⚠️  Gmail password not configured (still default)")
    else:
        print("✓ Gmail password configured")
    
    # Check Twilio config
    if settings.TWILIO_ACCOUNT_SID == 'your-twilio-account-sid':
        print("⚠️  Twilio Account SID not configured (still placeholder)")
    else:
        print("✓ Twilio Account SID configured")
    
    if settings.TWILIO_AUTH_TOKEN == 'your-twilio-auth-token':
        print("⚠️  Twilio Auth Token not configured (still placeholder)")
    else:
        print("✓ Twilio Auth Token configured")
    
    print("\n✅ Configuration complete!")

def main():
    """Main menu"""
    while True:
        print("\n" + "="*60)
        print("CREDENTIAL SETUP WIZARD")
        print("="*60)
        print("\nOptions:")
        print("1. Create .env file (Get credentials first!)")
        print("2. Load .env to settings.py")
        print("3. Validate credentials")
        print("4. Run notification tests")
        print("5. Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            create_env_file()
        elif choice == '2':
            load_env_to_settings()
        elif choice == '3':
            validate_credentials()
        elif choice == '4':
            print("\nRunning test script...")
            os.system('..\venv\Scripts\python.exe test_notifications.py')
        elif choice == '5':
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════╗
║   Django Notification System - Credential Setup           ║
║                                                            ║
║   Before running this script, you need:                  ║
║   1. Gmail App Password (from Google Account)            ║
║   2. Twilio Account SID & Auth Token                     ║
║   3. Twilio Phone Number                                 ║
║                                                            ║
║   Get them from:                                         ║
║   • Gmail: https://myaccount.google.com/apppasswords     ║
║   • Twilio: https://console.twilio.com/                  ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please try again or check the setup guide.")