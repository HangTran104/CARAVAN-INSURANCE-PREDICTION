from PIL import Image
from pytesseract import pytesseract
import enum
import glob

file_path = ['column_des_page1.png', 'column_des_page2.png', 'column_des_page3.png', 'column_des_page4.png', 'column_des_page5.png']
# files = glob.glob(path)

# class Language(enum.Enum):
#     ENG = 'eng'
#     RUS = 'rus'
#     ITA = 'ita'


class ImageReader:
    def __init__(self):
        win_path = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        pytesseract.tesseract_cmd = win_path
        print('Running:\n')

    def extract_text(self, image: str)->str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img)
        return extracted_text


if __name__ == '__main__':
    ir = ImageReader()
    pages_content = []
    for file in file_path:
        text = ir.extract_text('images/' + file)
        process_text = ' '.join(text.split())
        pages_content.append(process_text)

    print(pages_content)

    all_content = ' '.join(i for i in pages_content)

    with open('readme.txt', 'w') as f:
        f.write(all_content)




