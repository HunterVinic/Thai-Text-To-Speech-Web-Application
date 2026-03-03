# 🇹🇭 Thai Text-to-Speech Web Application

A Flask-based web application that converts text into Thai speech using the Vaja API from AI for Thai.

This application:
- Translates text to Thai (if needed)
- Sends text to Vaja Text-to-Speech API
- Generates a WAV audio file
- Plays the audio in the browser
- Allows users to download the generated file
- Supports Docker deployment

---

## 👨‍💻 Author

Sheshehang Limbu (HunterVinic)
September 21, 2023  

---

## 🚀 Features

- Thai Text-to-Speech conversion
- Automatic translation before speech generation
- WAV audio generation
- Web-based user interface
- Audio download functionality
- Docker container support

---

## 🛠 Tech Stack

- Python 3.9
- Flask
- Requests
- Wave
- Struct
- Translate
- Docker

---

## 📂 Project Structure

.
├── app.py (Flask application)
├── templates/
│   ├── index.html
│   └── test.html
├── audio/
│   └── output.wav
├── requirements.txt
├── Dockerfile
└── README.md

---

## 📦 Installation (Local)

1️⃣ Create virtual environment:

python -m venv venv
source venv/bin/activate

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Run application:

python app.py

4️⃣ Open browser:

http://localhost:8000

---

## 🐳 Run with Docker

Build image:

docker build -t thai-tts .

Run container:

docker run -p 8000:8000 thai-tts

Open:

http://localhost:8000

---

## 🔑 Environment Variable Setup (Recommended)

Instead of hardcoding API keys, create a `.env` file:

VAJA_API_KEY=your_real_key_here

Then modify your app to use:

import os
api_key = os.getenv("VAJA_API_KEY")

⚠️ Never commit API keys to GitHub.

---

## 📡 API Workflow

1. User enters text in web form
2. Text is optionally translated to Thai
3. Request sent to:
   https://api.aiforthai.in.th/vaja
4. Audio data received
5. WAV file generated
6. Audio played in browser
7. File available for download

---

## 🧾 Requirements.txt

Flask
requests
numpy
soundfile
translate

---

## 📌 Routes

### GET /
Displays the main text input page.

### POST /convert
Accepts JSON input:
{
  "text": "สวัสดี"
}

Returns:
{
  "success": true,
  "wav_url": "/download/speech.wav"
}

### GET /download/<filename>
Downloads generated audio file.

---

## 🔒 Security Notes

- Do NOT hardcode API keys
- Use environment variables
- Add `.env` to `.gitignore`
- Rotate API keys regularly
- Validate user input before API call

---

## 📈 Future Improvements

- Add async request handling
- Stream audio instead of saving to disk
- Add rate limiting
- Improve UI design
- Add language selector
- Store conversion history
- Deploy to AWS / GCP

---

## 📜 License

Copyright (c) 2026 Sheshehang Limbu

All rights reserved.

This project may not be copied, modified, distributed,
or used without explicit permission from the author.
