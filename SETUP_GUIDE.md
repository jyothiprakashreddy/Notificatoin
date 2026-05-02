# Setup Guide: Gmail App Password & Twilio Configuration

## Part 1: Gmail App Password Setup (2 minutes)

### Prerequisites:
- Gmail account (you're using: gampalajyothiprakash@gmail.com)
- 2-Factor Authentication enabled

### Steps:

**Step 1: Enable 2-Factor Authentication**
1. Go to https://myaccount.google.com/
2. Click "Security" in the left menu
3. Scroll down to "2-Step Verification"
4. Click "2-Step Verification"
5. Click "Get Started"
6. Follow the prompts to enable

**Step 2: Generate App Password**
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" for the app
3. Select "Windows Computer" for the device
4. Click "Generate"
5. Google will show a 16-character password
6. **COPY THIS PASSWORD** (remove spaces if present)

**Example Output:**
```
mfpx kgzp nmvq qwmx
→ mfpxkgzpnmvqqwmx (without spaces)
```

---

## Part 2: Twilio Account Setup (5 minutes)

### Steps:

**Step 1: Create Twilio Account**
1. Go to https://www.twilio.com/
2. Click "Sign up" (or "Get a Free Twilio Account")
3. Fill in your details:
   - First Name: Your Name
   - Last Name: Your Name
   - Email: Your Email
   - Password: Create a strong password
4. Verify your email
5. Create account

**Step 2: Get Account Credentials**
1. After login, go to Dashboard: https://console.twilio.com/
2. You'll see your Account SID and Auth Token on the dashboard
3. **SAVE THESE** (you'll need them)

**Step 3: Purchase a Phone Number**
1. In the Twilio Console, go to "Phone Numbers" → "Manage"
2. Click "Buy a Phone Number"
3. Select your country (US recommended for testing)
4. Choose a number (any available)
5. Click "Buy"
6. Note the phone number (format: +1234567890)

**Step 4: Verify Your Personal Phone (for testing)**
1. Go to "Phone Numbers" → "Verified Caller IDs"
2. Click "Add a new phone number"
3. Enter your personal phone number
4. Verify via SMS or call

---

## Part 3: Update Django Settings

Once you have all credentials, update `settings.py`:

```python
# Gmail Configuration
EMAIL_HOST_USER = 'gampalajyothiprakash@gmail.com'
EMAIL_HOST_PASSWORD = 'your-16-char-app-password'  # FROM STEP 1 PART 2

# Twilio Configuration
TWILIO_ACCOUNT_SID = 'your-account-sid'           # FROM STEP 2 PART 2
TWILIO_AUTH_TOKEN = 'your-auth-token'             # FROM STEP 2 PART 2
TWILIO_PHONE_NUMBER = '+1234567890'               # FROM STEP 3 PART 2
```

---

## Part 4: Test the Integration

After updating credentials:

```bash
# Navigate to project
cd user_notification

# Run test script
..\venv\Scripts\python.exe test_notifications.py

# Expected output:
# ✅ Email test successful
# ✅ SMS test successful
```

---

## Troubleshooting

### Gmail Issues
- **"Username and Password not accepted"**
  - Make sure you're using an APP PASSWORD, not regular password
  - Remove any spaces from the app password
  
- **2FA not enabled**
  - Gmail app passwords only work with 2FA enabled
  
- **Cannot find app passwords option**
  - Go directly to: https://myaccount.google.com/apppasswords

### Twilio Issues
- **"Authentication Error - invalid username"**
  - Check Account SID format (starts with "AC")
  - Check Auth Token has no spaces
  
- **SMS not sending**
  - Ensure phone number format is correct: +country code + number
  - Check Twilio account has trial credits
  - Verify phone numbers are in "Verified Caller IDs" for testing

### General
- **Check logs**: Review Django console output for error messages
- **Firewall**: Ensure outgoing connections are allowed
- **Rate limiting**: Wait between test attempts

---

## Quick Credential Checklist

```
Email:
☐ Gmail address: gampalajyothiprakash@gmail.com
☐ App password (16 chars, no spaces): ________________

Twilio:
☐ Account SID (starts with AC): ________________
☐ Auth Token (32+ chars): ________________
☐ Twilio Phone (+country): ________________
☐ Your phone (to test SMS): ________________
```

---

## Cost Breakdown

| Service | Cost | Notes |
|---------|------|-------|
| Gmail SMTP | Free | Unlimited emails |
| Twilio SMS | $0.0075/msg | ~$1 trial credit |
| Twilio Phone | $1/month | Includes 1000 SMS |
| **Total** | **~$1/month** | After trial |

---

## Security Best Practices

⚠️ **IMPORTANT**: Never commit credentials to Git!

1. Create `.env` file with sensitive data
2. Add `.env` to `.gitignore`
3. Never share credentials in code
4. Rotate credentials regularly
5. Use environment variables in production

Example `.env`:
```
EMAIL_HOST_PASSWORD=your-app-password
TWILIO_ACCOUNT_SID=your-account-sid
TWILIO_AUTH_TOKEN=your-auth-token
```

---

## Next Steps After Setup

1. ✅ Get Gmail app password
2. ✅ Create Twilio account and get credentials
3. ✅ Update settings.py with real values
4. ✅ Run test_notifications.py
5. ✅ Test appointment booking with real notifications
6. ✅ Deploy to production

