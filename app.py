from flask import Flask, request, render_template, jsonify
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

app = Flask(__name__, static_folder='.', static_url_path='')

# --- SETTINGS (Get these from developer.safaricom.co.ke) ---
CONSUMER_KEY = "your_consumer_key"
CONSUMER_SECRET = "your_consumer_secret"
PASSKEY = "your_stk_push_passkey"
# For Pochi, use the 254 format as the ShortCode
BUSINESS_SHORTCODE = "254769587139"
CALLBACK_URL = "https://yourdomain.com/callback" # Must be HTTPS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

def get_access_token():
    api_url = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_url, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))
    return r.json()['access_token']

@app.route('/pay-mpesa', methods=['POST'])
def pay_mpesa():
    phone = request.form.get('phone') # Customer's phone (e.g., 0712...)
    amount = request.form.get('amount', '100') # Default to 100 if not provided
    
    # Format phone to 254...
    if phone and phone.startswith("0"):
        phone = "254" + phone[1:]
    
    access_token = get_access_token()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode((BUSINESS_SHORTCODE + PASSKEY + timestamp).encode()).decode()
    
    headers = {"Authorization": f"Bearer {access_token}"}
    
    payload = {
        "BusinessShortCode": BUSINESS_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline", # Works for Pochi STK
        "Amount": amount,
        "PartyA": phone,
        "PartyB": BUSINESS_SHORTCODE,
        "PhoneNumber": phone,
        "CallBackURL": CALLBACK_URL,
        "AccountReference": "RichChickenHub",
        "TransactionDesc": "Chicken Order"
    }
    
    response = requests.post(
        "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
        json=payload,
        headers=headers
    )
    
    return jsonify(response.json())

@app.route('/pay-bitcoin', methods=['POST'])
def pay_bitcoin():
    # Placeholder for Bitcoin payment
    return jsonify({"status": "Bitcoin payment initiated"})


