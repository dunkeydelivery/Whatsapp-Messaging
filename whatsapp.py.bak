from flask import Flask, jsonify, request
import http.client
import json
import ssl

app = Flask(__name__)

class Ultrawebhook():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['data']


    def processing(self):
        if self.dict_messages != []:
            message = self.dict_messages
            msg_from = message['from'].split()
            msg_text = message['body'].split()
            print("sender phone number : " + msg_from[0])
            print(" ".join(msg_text))
            return ''


@app.route('/get_chat', methods=['POST'])
def get_chat():
    if request.method == 'POST':
        bot = Ultrawebhook(request.json)
        return bot.processing()



@app.route('/send_chat_message', methods=['POST'])
def send_chat_message():
    conn = http.client.HTTPSConnection("api.ultramsg.com", context=ssl._create_unverified_context())

    payload = {
        "token": "",
        "to": "+65 9232 4242",
        "body": "WhatsApp API on UltraMsg.com works good",
        "priority": 10,
        "referenceId": "",
        "msgId": "",
        "mentions": ""
    }
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        payload_json = json.dumps(payload)
        conn.request("POST", "/instance45364/messages/chat", payload_json, headers)
        res = conn.getresponse()
        data = res.read()
        response_data = data.decode("utf-8")
        return jsonify({"message": "Chat message sent successfully", "response_data": response_data})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if(__name__) == '__main__':
    app.run(debug=True, port=8000)



