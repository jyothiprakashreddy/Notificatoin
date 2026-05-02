# Quick Start: Gmail + Twilio Setup (10 minutes)

## 🚀 Quick Links
- **Gmail App Password**: https://myaccount.google.com/apppasswords
- **Twilio Console**: https://console.twilio.com/
- **Twilio Phone Numbers**: https://console.twilio.com/phone-numbers/incoming

---

## ⚡ GMAIL SETUP (2 minutes)

### Quick Checklist:
- [ ] Go to https://myaccount.google.com/
- [ ] Click "Security" → "2-Step Verification" (enable if needed)
- [ ] Go to https://myaccount.google.com/apppasswords
- [ ] Select: Mail + Windows Computer
- [ ] Click "Generate"
- [ ] Copy the 16-character password (remove spaces)

**Example**: `mfpx kgzp nmvq qwmx` → Copy as: `mfpxkgzpnmvqqwmx`

✅ **You'll have**: `mfpxkgzpnmvqqwmx`

---

## ⚡ TWILIO SETUP (5 minutes)

### Step 1: Create Account
- [ ] Go to https://www.twilio.com/
- [ ] Click "Sign Up"
- [ ] Fill in details and verify email

### Step 2: Get Account Credentials
- [ ] Login to https://console.twilio.com/
- [ ] Copy "Account SID" (starts with `AC...`)
- [ ] Copy "Auth Token" (long string)

**Example Account SID**: `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
**Example Auth Token**: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Step 3: Buy a Phone Number
- [ ] Go to https://console.twilio.com/phone-numbers/incoming
- [ ] Click "Buy a Number"
- [ ] Select Country: United States
- [ ] Pick any number
- [ ] Click "Buy" (free trial credit)

**Example**: `+12025551234`

✅ **You'll have**:
- Account SID: `AC...`
- Auth Token: `...`
- Twilio Phone: `+12025551234`

---

## 🔧 CONFIGURATION (1 minute)

### Option A: Interactive Setup (Recommended)

```bash
cd user_notification
..\venv\Scripts\python.exe setup_credentials.py
```

Then select **Option 1** to enter credentials.

### Option B: Manual Setup

Edit `user_notification/settings.py` and replace:

```python
# Line 128 - Gmail
EMAIL_HOST_PASSWORD = 'mfpxkgzpnmvqqwmx'

# Lines 131-133 - Twilio  
TWILIO_ACCOUNT_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
TWILIO_AUTH_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
TWILIO_PHONE_NUMBER = '+12025551234'
```

---

## ✅ TEST (2 minutes)

```bash
cd user_notification
..\venv\Scripts\python.exe test_notifications.py
```

**Expected Output**:
```
✅ Email test successful
✅ SMS test successful
```

---

## 🎯 FULL TEST: Appointment Booking

1. Start server:
```bash
cd user_notification
..\venv\Scripts\python.exe manage.py runserver
```

2. Go to: http://127.0.0.1:8000/appointment/

3. Fill form with **YOUR REAL PHONE/EMAIL**:
   - Name: Your Name
   - Day: Monday
   - Phone: +1234567890 (YOUR REAL NUMBER)
   - Email: your@email.com (YOUR REAL EMAIL)

4. Click Submit

5. Check:
   - ✅ Email inbox
   - ✅ Phone (SMS)

---

## ❌ TROUBLESHOOTING

### Gmail Issues
- **"Username and Password not accepted"**
  - You used regular password instead of App Password
  - Go to https://myaccount.google.com/apppasswords
  - Generate new password

- **2FA error**
  - Enable 2-Step Verification first
  - App passwords only work WITH 2FA

### Twilio Issues
- **"Authentication Error"**
  - Account SID has spaces
  - Auth Token is incorrect
  - Copy again from dashboard

- **SMS not sending**
  - Phone format must be: `+1234567890`
  - Add country code (+1 for US)
  - Check trial balance in dashboard

---

## 💡 TIPS

✅ **Save credentials securely** - Use `.env` file
✅ **Never commit passwords** - Add `.env` to `.gitignore`
✅ **Test with your real info** - Use your actual phone/email
✅ **Check spam folder** - Emails might go there
✅ **Monitor Twilio balance** - ~$0.0075 per SMS

---

## 📝 CREDENTIAL FORM

Print this and fill it in:

```
Gmail Email: gampalajyothiprakash@gmail.com
Gmail App Password: ________________

Twilio Account SID: ________________
Twilio Auth Token: ________________
Twilio Phone Number: ________________

Your Test Phone: ________________
Your Test Email: ________________
```

---

**Ready?** Run this command:
```bash
cd c:\Users\G.Jyothiprakashreddy\OneDrive\Documents\GitHub\Notificatoin\user_notification
..\venv\Scripts\python.exe setup_credentials.py
```