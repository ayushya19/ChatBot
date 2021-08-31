import os
import PyPDF2

files = []
# all = os.listdir('./')
# for i in all:
#     if '.pdf' in i:
#         files.append(i)

# print(files)

files.append('./fesc112.pdf')

for pdf in files:
    pdfobj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfobj)
    x = pdfReader.numPages
    pageObj = pdfReader.getPage(x-1)

    text = pageObj.extractText()
    file1 = open('ElectricityCorpus.txt', 'a')
    file1.writelines(text)
