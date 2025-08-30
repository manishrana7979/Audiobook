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
<ul>  
<li>PdfReader('Suno_kahani.pdf') → Opens and parses your PDF.</li>
<li>reader.pages[2] → Gets the 3rd page object.</li>
<li>page.extract_text() → Extracts all readable text from that page.</li>
<li>pyttsx3.init() → Initializes the speech engine.</li>
<li>speak.say(text) → Passes the text to be spoken.</li>
<li>speak.runAndWait() → Actually speaks it out loud.</li>
</ul>

How to RUN:

<ul>
<li>Step 1 
  You need to install pythsx3 in your system.
  Run <b>pip3 install pyttsx3</b> in your terminal.</li>
</ul>
