# Text_to_Speech
A simple Python project that converts PDF text into speech. It uses pypdf to extract text from PDF files and pyttsx3 to read it aloud, turning any PDF into an audiobook.

What your code is trying to do

Import libraries:
<ul>
  
<li>pyttsx3 → Python text-to-speech library.</li>

<li>pypdf.PdfReader → Reads PDF files.</li>

<li>Read PDF: You want to open suno_kahani.pdf and get text from the 3rd page (Python uses zero-based indexing, so page[0] means page 1).</li>

<li>Convert text to speech: Using pyttsx3 to read the extracted text aloud.</li>
</ul>

How this works (step-by-step)

PdfReader('Manish_Data_Entry.pdf') → Opens and parses your PDF.

reader.pages[2] → Gets the 3rd page object.

page.extract_text() → Extracts all readable text from that page.

pyttsx3.init() → Initializes the speech engine.

speak.say(text) → Passes the text to be spoken.

speak.runAndWait() → Actually speaks it out loud.
