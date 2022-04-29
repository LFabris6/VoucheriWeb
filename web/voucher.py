
import shutil
import os
import gspread
from mailmerge import MailMerge
from PyPDF2 import PdfFileMerger
import comtypes.client
from django.contrib import messages

template = "static/api/voucher.docx"

def create(od, do, sheet, request):
    try:
        gc = gspread.service_account(filename='static/api/client.json')
        sh = gc.open_by_key('1A41ogDqUWtHUALXmBpjP8Sj_ZRN8mq9c7t43LjYm2x4')
        worksheet = sh.get_worksheet(sheet-1)
    except:
        return -1


    for i in range(od, do+1):
        ime = worksheet.cell(i, 1).value
        prezime = worksheet.cell(i, 2).value
        broj = worksheet.cell(i, 3).value
        gmail =  worksheet.cell(i, 4).value
        datum =  worksheet.cell(i, 5).value
        ispuni(ime, prezime, broj, gmail, datum)
    
    comtypes.CoInitialize()
    word = comtypes.client.CreateObject('Word.Application')
    pdfslist = PdfFileMerger()
    x = 0

    directory = 'D:/Pro/mp/adriaticweb/static/voucheri/'

    for filename in os.listdir(directory):
        print(filename)
        f = os.path.join(directory, filename)
        output_file = docx_to_pdf(word, f, x)
        pdfslist.append(open(output_file, 'rb'))
        x += 1
        
    word.Quit()

    with open("static/finals/final.pdf", "wb") as result_pdf:
        pdfslist.write(result_pdf)
        pdfslist.close()


    ocisti()
   
    return 0
def docx_to_pdf(word, file, x):
    print(file)
    input_file = os.path.abspath(file)
    output_file = os.path.abspath("demo" + str(x) + ".pdf")
    doc = word.Documents.Open(input_file)
    doc.SaveAs(output_file, FileFormat=16+1)
    doc.Close() 
    return output_file
def ispuni(ime, prezime, broj, gmail,datum):
    print("kreiramo voucher za" + ime)
    document = MailMerge(template)
    document.merge(Ime=ime, prezime=prezime, email=gmail, broj = broj, rodenje=datum)
    path = "static/voucheri/voucher" + str(broj) + ".docx"
    document.write(path)
def ocisti():
    dir = "static/voucheri/"
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_dir() and not entry.is_symlink():
                shutil.rmtree(entry.path)
            else:
                os.remove(entry.path)