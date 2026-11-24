
from flask import Flask

app = Flask(__name__)

app.add_url_rule("/", "chat", lambda: "Hello! I'm the mini chatbot for the Cloud Infrastructure Management class. How can I help you?")

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000)

