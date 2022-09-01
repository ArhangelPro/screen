import pyscreenshot
from tkinter import *
import pyautogui
import datetime
import pytesseract
from PIL import Image  

image = pyscreenshot.grab()
image.show()
image.save("fileName.png")

print("Текс найден, распознаю")
img = Image.open('fileName.png')

file_name = img.filename
file_name = file_name.split(".")[0]

print(file_name)

text = pytesseract.image_to_string(img, lang='rus').strip()

print(text)
with open(f'{file_name}.txt', 'w') as text_file:
    text_file.write(text)

