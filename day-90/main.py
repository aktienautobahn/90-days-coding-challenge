import io
import os
import requests
import base64
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from PyPDF2 import PdfFileReader

# Load the credentials
credentials = service_account.Credentials.from_service_account_file('service_account.json')

if credentials.expired:
    credentials.refresh(Request())

# Get the access token
access_token = credentials.token

# Extract the text from the PDF
def extract_text_from_pdf(file_path):
    pdf = open(file_path, "rb")
    pdf_reader = PdfFileReader(pdf)
    text = ""
    for page in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page).extract_text()
    pdf.close()
    return text

# Convert text to speech
def convert_text_to_speech(text, access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json; charset=utf-8'
    }
    data = {
        'input': {
            'text': text
        },
        'voice': {
            'languageCode': 'en-gb',
            'name': 'en-GB-Standard-A',
            'ssmlGender': 'FEMALE'
        },
        'audioConfig': {
            'audioEncoding': 'MP3'
        }
    }
    response = requests.post("https://texttospeech.googleapis.com/v1/text:synthesize", headers=headers, json=data)
    audio_content = response.json()['audioContent']
    return base64.b64decode(audio_content)

# Save the speech audio into a file
def save_speech_to_file(speech_audio, file_path):
    with open(file_path, "wb") as audio:
        audio.write(speech_audio)

# Define your PDF file path
pdf_file_path = 'your_pdf_file.pdf'
# Extract text
text = extract_text_from_pdf(pdf_file_path)
# Convert text to speech
speech_audio = convert_text_to_speech(text, access_token)
# Save the speech audio into a file
save_speech_to_file(speech_audio, 'output.mp3')
