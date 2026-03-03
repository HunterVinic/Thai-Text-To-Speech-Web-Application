import os
import requests
from flask import Flask, render_template, request, send_file
from translate import Translator

app = Flask(__name__)


def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation


sample_rate = 44100
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Replace with your actual API key
api_url = 'https://api.aiforthai.in.th/vaja'


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]

        translated_text = translate_text(text, "th")
        print("Translated text:", translated_text)

        # Prepare the API request parameters
        headers = {
            'Apikey': api_key,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {
            'text': translated_text,
            'mode': 'st'
        }

        # Send a POST request to the API to get the audio
        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            # Save the audio data to a file
            audio_output_path = "/app/audio/output.wav"
            with open(audio_output_path, 'wb') as audio_file:
                audio_file.write(response.content)

            # Get the duration of the generated audio
            audio_duration = len(response.content) / (sample_rate * 2)  # Assuming 16-bit stereo audio

            return render_template("index.html", audio_path=audio_output_path, audio_duration=audio_duration)
        else:
            return "Error: Text-to-speech conversion failed."

    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():
    audio_path = request.form["audio_path"]
    return send_file(audio_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
