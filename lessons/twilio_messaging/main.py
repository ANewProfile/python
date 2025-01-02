from twilio.rest import Client
import keys

account_sid = keys.account_sid
auth_token = keys.auth_token
phone_number = keys.phone_number

client = Client(account_sid, auth_token)
message = client.messages.create(
  from_=phone_number,
  body='Hello world!',
  to='+16176861000'
)

print(message.sid)