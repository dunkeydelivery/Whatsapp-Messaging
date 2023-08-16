from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from flask import Flask, request

# Twilio credentials
account_sid = ''
auth_token = ''

# Create a Flask app
app = Flask(__name__)

# Sending a WhatsApp message
def send_whatsapp_message(to_number, message):
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
                            body=message,
                            from_='whatsapp:+14155238886',
                            to='whatsapp:'+to_number
                        )
        print('Message sent:', message.sid)
    except Exception as e:
        print('Error sending WhatsApp message:', str(e))

# Receiving a WhatsApp message
@app.route('/webhook', methods=['POST'])
def receive_whatsapp_message():
    body = request.form.get('Body', '')
    sender = request.form.get('From', '')
    message = f'Received message "{body}" from {sender}'

    # Process the received message
    # ...

    # Send a response
    response = MessagingResponse()
    response.message('Thank you for your message!')

    return str(response)

# Example usage
if __name__ == '__main__':
    app.run()

# Sending a message
to_number = '+6592324242'
message = 'Hello SAM, This is AISE, How can i help you today?'
send_whatsapp_message(to_number, message)