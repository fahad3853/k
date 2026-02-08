from flask import Flask, render_template
import random

app = Flask(__name__)

messages = [
    "You are the most beautiful part of my life ❤️",
    "Every moment with you feels magical ✨",
    "I fall in love with you again every day 💕",
    "You are my peace, my happiness, my home 🏡❤️"
]

@app.route("/")
def home():
    message = random.choice(messages)
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)


