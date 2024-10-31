import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os

filename = "north_korea_economin_growth.pdf"
filepath = os.path.join(os.getcwd(), "data", filename)

# PdfReader로 총 페이지 수 얻기
fp = open(filepath, 'rb')
reader = PyPDF2.PdfReader(fp)
total_pages = len(reader.pages)
print(total_pages)

page_text = {}
for page_no in range(total_pages):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    # PdfMiner 설정
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

# 첫 번째 페이지 출력
print(page_text[0][:-1])
