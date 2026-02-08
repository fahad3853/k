import os
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

wife_name = "Kulsum"

messages = [
    "Kulsum, you are the most beautiful part of my life ❤️",
    "Every moment with you feels magical, my Kulsum ✨",
    "I fall in love with you again every single day, Kulsum 💕",
    "Kulsum, you are my peace, my happiness, my home 🏡❤️",
    "No matter where I am, my heart is always with you, Kulsum 💖"
]

@app.route("/")
def home():
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good Morning, Kulsum ☀️"
    elif hour < 18:
        greeting = "Good Afternoon, My Love 💕"
    else:
        greeting = "Good Night, Kulsum 🌙❤️"

    # ✅ Send the full messages list
    return render_template(
        "index.html",
        messages=messages,
        greeting=greeting,
        name=wife_name
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
