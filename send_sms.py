from twilio.rest import Client

account_sid = "AC1032937868d62045d11835449e83bd1a"
auth_token = "0cdbe99ab6d4df8cf40918d6d6eb19f2"

client = Client(account_sid, auth_token)

#call = client.calls.create(
#    to = "+15123630687",
#    from_="+16284000095",
#    url="http://demo.twilio.com/docs/voice.xml"
#)

message = client.messages.create(
    to="+15123630687",
        from_="+16284000095",
    body = "Hello there!"
)

#print(call.sid)
