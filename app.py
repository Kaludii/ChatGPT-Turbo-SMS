import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set up your Twilio credentials and OpenAI API key
twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]
openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route("/sms", methods=["POST"])
def sms_reply():
    user_msg = request.form.get("Body")

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_msg}
        ]
    )

    gpt_reply = response['choices'][0]['message']['content']

    # Send the response back as an SMS
    twiml = MessagingResponse()
    twiml.message(gpt_reply)
    return str(twiml)

if __name__ == "__main__":
    app.run(debug=True)
