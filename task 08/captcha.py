from PIL import Image
import pytesseract


text = pytesseract.image_to_string(Image.open("captcha.jpg"))

print(int(text[0])+int(text[2]))
