"""
Thai Text-to-Speech Converter Documentation

This Flask web application allows users to convert Thai text input into speech and provides the option to download
the generated audio file.

Author: Sheshehang Limbu
Date: September-21-2023

Usage:
1. Start the Flask application by running this script.
2. Access the web interface by visiting http://localhost:8000/ in your web browser.
3. Enter Thai text into the textarea and click the "Convert" button.
4. The converted audio will be played and available for download.

Dependencies:
- Flask: A Python web framework for building web applications.
- requests: A library for making HTTP requests.
- wave: A module for working with WAV audio files.
- struct: A module for working with binary data.

Routes:
- '/' (Index):
  - Renders the main web page for the Thai Text-to-Speech Converter.
  - Related HTML: 'test.html'

- '/convert' (POST):
  - Accepts POST requests with JSON data containing the input text.
  - Calls the Vaja API to convert the text to speech.
  - Generates a WAV audio file from the API response.
  - Provides a download link for the generated audio.

- '/download/<filename>' (GET):
  - Allows users to download the generated audio file.

Components:
- API_KEY: 'qJJe9qkPbJrwXC0KSeZQdjST1mvVIsv7'
- 'index' route: Renders the main web page (test.html) where users can input text.
- 'convert_text_to_speech' route (POST): Converts input text to speech and generates a downloadable audio file.
- 'download_file' route (GET): Allows users to download the generated audio file.
- 'test.html': HTML template for the web page with input form and download button.
- JavaScript: Handles form submission, API request, and audio playback/download.

Styles:
- CSS styles are applied to the HTML elements for a visually appealing interface.
- Styles include textareas, buttons, audio player, and download button.

Notes:
- Make Sure that the 
- Ensure that you have the required dependencies installed before running the application.
- Customize the CSS styles as needed for your project's design.
"""

# Import necessary libraries
from flask import Flask, request, jsonify, send_file, render_template
import requests
import wave
import struct

app = Flask(__name__)

# Replace with your Vaja API key
API_KEY = 'qJJe9qkPbJrwXC0KSeZQdjST1mvVIsv7'

# Define the main route that renders the web page
@app.route('/')
def index():
    return render_template('test.html')

# Define the route for converting text to speech
@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.get_json()
    input_text = data.get('text', '')

    # Call the Vaja API to get the speech data
    url = 'https://api.aiforthai.in.th/vaja'
    headers = {
        'Apikey': API_KEY,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params = {
        'text': input_text,
        'mode': 'st'
    }
    response = requests.get(url, params=params, headers=headers)
    vaja_data = response.json()

    if 'output' in vaja_data and 'audio' in vaja_data['output']:
        result = vaja_data['output']['audio']['result']
        valid_bits = vaja_data['output']['audio']['validBits']
        sample_rate = vaja_data['output']['audio']['sampleRate']
        size_sample = vaja_data['output']['audio']['sizeSample']

        # Create a WAV file using Vaja-style code
        wav_filename = 'speech.wav'
        with wave.open(wav_filename, 'wb') as wav_file:
            wav_file.setparams((1, valid_bits // 8, sample_rate, 0, 'NONE', 'not compressed'))
            for i in range(size_sample):
                value = int(result[i])
                data = struct.pack('<h', value)
                wav_file.writeframesraw(data)

        wav_url = f'/download/{wav_filename}'

        return jsonify({'success': True, 'wav_url': wav_url})

    return jsonify({'success': False, 'error': 'Conversion failed'}), 400

# Define the route for downloading the generated audio file
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

# Run the Flask application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
