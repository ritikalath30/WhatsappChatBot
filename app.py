from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse,Body,Message,Redirect

from utils import fetch_reply

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get("Body")
    phone_no = request.form.get("From")
    reply = fetch_reply(msg,phone_no)
    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)