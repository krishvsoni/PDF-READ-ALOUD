
import pyttsx3
import PyPDF2

book=open('11th Eng. Med. - Chemistry - IUPAC Name - 2 - Answer Key.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages= pdfReader.numPages
print(pages)


speaker=pyttsx3.init()

for num in range(4,pages):
    page = pdfReader.getpage(4)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()