from flask import Flask, request, redirect, render_template
import os
from twilio.rest import Client

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/make-call", methods=["POST"])
def make_call():
    phone_number = request.form.get("phone_number")
    account_sid = "ACcae4454ffa2c5db7f5f368cec0ef4af0"
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        url="https://wise-agent.onrender.com/voice",
        to=phone_number,           
        from_="+19895192066" )

    print(call.sid)
    return redirect("/")  

if __name__ == "__main__":
    app.run(debug=True)