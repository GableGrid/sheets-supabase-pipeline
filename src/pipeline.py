import gspread
from google.oauth2.service_account import Credentials
import requests

# Google Sheets Authentication
JSON_FILE = "credentials.json"
SHEET_ID = "1gwQc7xDulDfw1ES37SmsWJwECHg-oEdOVADYdCnzrE8"

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file(JSON_FILE, scopes=scope)
client = gspread.authorize(creds)

# Read data from Google Sheet
sheet = client.open_by_key(SHEET_ID).sheet1
data = sheet.get_all_records()
print(f"Read {len(data)} rows from Google Sheet")

# Supabase API details
SUPABASE_URL = "https://skvmpqoidojelhfzdnpn.supabase.co/rest/v1"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNrdm1wcW9pZG9qZWxoZnpkbnBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNzgzNzAsImV4cCI6MjA5Mzk1NDM3MH0.yJeaZQVMEkps1VljUV5LwPOYmuysMpzpv70IKpvr1mw"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

# Convert phone to string
for row in data:
    row["phone"] = str(row["phone"])

# Insert data into Supabase
response = requests.post(
    f"{SUPABASE_URL}/contacts",
    headers=headers,
    json=data
)

print("Status:", response.status_code)
print("Done!")