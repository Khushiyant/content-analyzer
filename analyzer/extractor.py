import pytesseract
from PIL import Image


class text_extract:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    def processing(self, imgSrc):
        img = Image.open(imgSrc)
        text = pytesseract.image_to_string(img, lang='eng')
        return text

