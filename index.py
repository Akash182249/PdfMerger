from PyPDF2 import PdfFileMerger
import os 

merger = PdfFileMerger()
for items in os.listdir():
  if items.endswith('.pdf'):
    merger.append(items)
#The merged pdf file will save in the same folder
merger.write("trashismerged_pdf.pdf")
merger = PdfFileMerger()
with open(originalFile, 'rb') as fin:
    merger.append(PdfFileReader(fin))
os.remove(originalFile)
merger.close()
# Enjoy!