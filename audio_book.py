import pyttsx3 #import librery text to speech
from pypdf import PdfReader

# Load PDF file
reader = PdfReader('suno_kahani.pdf')

# Extract text from page 1 (index starts at 0)
page = reader.pages[0]
text = page.extract_text()

# Initialize text-to-speech engine
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
