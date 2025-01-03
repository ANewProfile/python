from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import keys

# NEED TO SETUP OAUTH2 AND GET CREDENTIALS
def check_unread():
    service = build('gmail', 'v1', credentials=keys.creds)
    results = service.users().messages().list(
        userId='me', 
        q='is:unread'
    ).execute()

    return results.get('messages', [])