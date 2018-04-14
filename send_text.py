from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf9e6f9ccaf5ec64d9cde0b3f6f861e3e"
# Your Auth Token from twilio.com/console
auth_token  = "55be4c5a269125f54ee077134017a252"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18596407704",
    from_="+15138540394",
    body="Hello from Python!")

print(message.sid)
