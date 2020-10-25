import pyttsx3
import PyPDF2

class Read_PDF ():
    def __init__ (self, file, page = 0):
        self.file = file
        self.page = page
        self.text = self.convert()

    def clean_text (self, text_str):
        return text_str.replace("\n", "")

    def convert (self):
        with open("PDFs/%s" % self.file, "rb") as f:
            converted = PyPDF2.PdfFileReader(f)
            text_str = converted.getPage(self.page).extractText()
            cleaned_text = self.clean_text(text_str)
            print(cleaned_text)
        return cleaned_text

    def read (self):
        speaker = pyttsx3.init()
        speaker.say(self.text)
        speaker.runAndWait()
        user_response = input("Press enter/return for next page, 'r' to reread, or 'x' to end: ")
        if user_response == "":
            self.page += 1
            self.text = self.convert()
            self.read()
        elif user_response == "r":
            self.read()
        else:
            return None

to_read = input("Enter the pdf name (ex. my_book.pdf): ")
start_page = input("Enter starting page number, or press Enter to start from the beginning: ")

def convert_start_page (start_str):
    try:
        page = int(start_str) - 1
    except:
        page = 0
    return page

pdf_str = Read_PDF(to_read, convert_start_page(start_page))
pdf_str.read()
