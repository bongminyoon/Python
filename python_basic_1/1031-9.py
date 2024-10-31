import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os


def pdf_to_txt(filepath):
    # PyPDF2를 사용해 총 페이지 수 확인
    fp = open(filepath, 'rb')
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
        fp = open(filepath, 'rb')
        password = None
        maxpages = 0
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        caching = True
        pagenos = [page_no]

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            interpreter.process_page(page)
        page_text[page_no] = retstr.getvalue()

        # 리소스 정리
        fp.close()
        device.close()
        retstr.close()

    return page_text


if __name__ == "__main__":
    filename = "north_korea_economic_growth.pdf"
    filepath = os.path.join(os.getcwd(), "data", filename)
    pdf_text = pdf_to_txt(filepath)

    # 결과를 텍스트 파일로 저장
    text_file = os.path.join(os.getcwd(), "output", filename.split('.')[0] + ".txt")
    with open(text_file, 'w', encoding="utf-8") as f:
        for k, v in pdf_text.items():
            first_row = "------------------------%s 페이지의 내용입니다------------------------- \n" % k
            f.write(first_row + v)
