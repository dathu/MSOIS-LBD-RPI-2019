from PIL import Image
import pytesseract

im = Image.open("img3.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')
print(text)


