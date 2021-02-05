"""
Author: Madhu Babu Kencha

This script reads the text on the image and converts that text
into speech
"""
# Python tesseract is an Optical Character Recognition(OCR) tool
# for python. That is, it will recognize and "read" the text em-
# bedded in images
import pytesseract
# This module adds the image processing capabilities
from PIL import Image
# Use pyttsx3==2.71, higher versions causing issues
# To convert text to speech
import pyttsx3
# It will translates the input into desired language
from google_trans_new import google_translator


def read_image(image_path):
    """
    Function to read text from image
    """
    # Opening image
    # <PIL.PngImagePlugin.PngImageFile image mode=L size=336x150 at 0x2755CC22CC8>
    img = Image.open(image_path)

    # We have to set path for module tesseract(Need to install tesseract executable)
    # executable tesseract link or else I will provide file here
    # https://github.com/UB-Mannheim/tesseract/wiki
    tesseract_exe = r"C:\Users\kench\AppData\Local\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = tesseract_exe
    text = pytesseract.image_to_string(img)
    return text


def read_text(text_to_read):
    """
    Function to convert text to speech
    """
    engine = pyttsx3.init()
    engine.say(text_to_read)
    engine.runAndWait()


def translate_text(text_to_trans, lang_to_trans):
    """
    Function to translate text
    """
    translator = google_translator()
    converted_text = translator.translate(text_to_trans, lang_tgt=lang_to_trans)
    return converted_text


if __name__ == '__main__':
    img_path = r"D:\Programming_Languages\Python\General_Purpose\img_text_to_speech\images\text_image.png"
    text = read_image(img_path)
    print(text)
    read_text(text)
    # Converting in text into telugu
    trans_text = translate_text(text, "te")
    print(trans_text)
