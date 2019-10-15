# This converter code is not mine - it has been retrieved from:
# https://github.com/mgorkove/tutorials/blob/master/Using-Python-to-Convert-PDFs-to-Text-Files/pToT.py


import pdfminer
import os
import sys, getopt
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert(filename, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
   
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    
    infile = open(filename, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

#test = convert("Argentina_BuenosAires_092818.pdf")

#test

#fileobj = open("Argentina_BuenosAires_092818.txt", "w", encoding="utf-8")
#fileobj.write(test)

def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w", encoding="utf-8") #make text file
            textFile.write(text) #write text to text file
            
sourcedir = r"C:\Users\garre\OneDrive\Northeastern\Research_Projects\100_Resilient_Cities_Topic_Model\Docs\PDFs\\"
exitdir = r"C:\Users\garre\OneDrive\Northeastern\Research_Projects\100_Resilient_Cities_Topic_Model\Docs\Raw_Texts\\"

convertMultiple(sourcedir, exitdir)