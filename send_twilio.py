from twilio.rest import TwilioRestClient

account_sid = "ACf92e780ed47fb4f4141ac08f72117330" # Your Account SID from www.twilio.com/console
auth_token  = "d36816f3f0dbde17184f08cf5b359203"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hi sexy! How are you doing? :-)",
    to="+17872146002",    # Replace with your phone number
    from_="+17873392168") # Replace with your Twilio number

print(message.sid)
