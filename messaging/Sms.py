from twilio.rest import Client

account_sid = 'AC8e504ecec8a7d7e2019100856b141265'
auth_token = '2483ac25bee9f24f0a907c08f40d67e3'
client = Client(account_sid, auth_token)

def send_message(body="Test message using Twilio API"):
    message = client.messages.create(
        from_='+15155005604',
        to='+918700049770',
        body=body
    )

    print(message.sid)


if __name__=="__main__":
    send_message("Hi FROM Python")