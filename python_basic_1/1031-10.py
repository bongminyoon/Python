import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os


def pdf_to_txt(filepath):
    # PdfReader로 파일 읽기 및 페이지 수 가져오기
    with open(filepath, 'rb') as fp:
        reader = PyPDF2.PdfReader(fp)
        total_pages = len(reader.pages)
        page_text = {}

        for page_no in range(total_pages):
            # PDFMiner 리소스 설정
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)

            # PDF 페이지 해석기 설정
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            pagenos = [page_no]

            for page in PDFPage.get_pages(fp, pagenos, caching=True, check_extractable=True):
                interpreter.process_page(page)
            page_text[page_no] = retstr.getvalue()

            # 리소스 정리
            device.close()
            retstr.close()

    return page_text


folder_path = os.path.join(os.getcwd(), "data", "pdf")
file_list = os.listdir(folder_path)

for file_name in file_list:
    pdf_text = pdf_to_txt(os.path.join(folder_path + "\\" + file_name))
    text_file = os.path.join(folder_path, file_name.split(".")[0] + ".txt")

    with open(text_file, 'w', encoding="utf-8") as f:
        for v in pdf_text.values():
            f.write(v)

    print(f"{file_name.split('.')[0]}.txt 파일이 저장되었습니다 \n")
