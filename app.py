# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

wife_name = "For Kulsum"

# Rahat Indori style Hinglish shayari with emojis
messages = [
    "Suno na kuch kehna hai 💖",
    "Tumhare bin zindagi adhoori hai, tum ho to har pal poora hai 💖",
    "Har lamha tumhare khayalon mein, jaise mehfil mein chandni ✨",
    "Main apni har dua mein sirf tumhara naam leta hoon 💕",
    "Tum meri khushi ho, meri jaan ho, meri pehchan ho 🏡💖",
    "Tumhari muskaan meri sabse badi daulat hai 💖",
    "Dil yeh kehta hai bas tum hi tum ho, aur kuch nahi 💖",
    "Tumhare pyaar ka ehsaas har pal mehsoos karta hoon 💕",
    "Tum meri zindagi ka wo haseen lamha ho jo kabhi khatam na ho 🏡💘",
    "Main tumhe har pal chahunga, chahe din ho ya raat 🌙✨",
    "Tum meri dhadkan mein ho, meri rooh mein ho, meri duniya mein ho 💖",
    "Tumhare bina har raasta suna, har khushi adhoori hai 💔❤️",
    "Main har pal tumse mohabbat karta hoon, jaise shayari mein alfaaz 💕",
    "Tum meri har khushi ka sabab ho, meri har dua ka jawab ho 🏡💖",
    "Zindagi ke har mod par sirf tumhara saath chahiye 💖",
    "Tum meri aankhon ka noor ho, meri har khushi ka ehsaas ho ✨"
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

    # Send the full messages array to index.html
    return render_template(
        "index.html",
        messages=messages,
        greeting=greeting,
        name=wife_name
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


