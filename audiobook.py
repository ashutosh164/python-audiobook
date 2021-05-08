import pyttsx3
import PyPDF2

book = open('Audio book/oop.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
pages= pdf_reader.numPages
print(pages)

speaker = pyttsx3.init()
page = pdf_reader.getPage(7)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()