# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

title_name = "For Kulsum"
heading_name = "Meri Pyari Biwi Jaan (Kulsum)"

# Rahat Indori style Hinglish shayari with emojis
messages = [
    "Suno na kuch kehna hai 💖",
    "Tumhare bin zindagi adhoori hai, tum ho to har pal poora hai 💖",
    "Har lamha tumhare khayalon mein, jaise mehfil mein chandni ✨",
    "Main apni har dua mein sirf tumhara naam leta hoon 💕",
    "Tum meri khushi ho, meri jaan ho, meri pehchan ho 🏡💖",
    "Tumhari muskaan meri sabse badi daulat hai 💖",
    "Dil yeh kehta hai bas tum hi tum ho, aur kuch nahi 💖"
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

    return render_template(
        "index.html",
        messages=messages,
        greeting=greeting,
        title_name=title_name,
        heading_name=heading_name
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
