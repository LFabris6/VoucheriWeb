
import shutil
import os
import gspread
from mailmerge import MailMerge
from PyPDF2 import PdfFileMerger
from django.contrib import messages
from docx2pdf import convert
import docx2pdf

template = "static/api/voucher.docx"

def create(od, do, sheet, request):
    
    try:
        gc = gspread.service_account(filename='static/api/client.json')
        sh = gc.open_by_key('1A41ogDqUWtHUALXmBpjP8Sj_ZRN8mq9c7t43LjYm2x4')
        worksheet = sh.get_worksheet(sheet-1)
    except:
        return -1

    pdfslist = PdfFileMerger()
    for i in range(od, do+1):
        ime = worksheet.cell(i, 1).value
        prezime = worksheet.cell(i, 2).value
        broj = worksheet.cell(i, 3).value
        gmail =  worksheet.cell(i, 4).value
        datum =  worksheet.cell(i, 5).value
        ispuni(ime, prezime, broj, gmail, datum, pdfslist)
    
    with open("static/finals/final.pdf", "wb") as result_pdf:
        pdfslist.write(result_pdf)
        pdfslist.close()


    ocisti()
   
    return 0


def ispuni(ime, prezime, broj, gmail,datum, pdfslist):
    try:
        print("pocetak docx " + ime)
        document = MailMerge(template)
        document.merge(Ime=ime, prezime=prezime, email=gmail, broj = broj, rodenje=datum)
        path = "static/voucheri/voucher" + str(broj) + ".docx"
        output_file = "static/voucheri/voucher" + str(broj) + ".pdf"
        document.write(path)
        print("docx sejvan " + ime)
        convert(path)
        print("d " + ime)
        pdfslist.append(open(output_file, 'rb'))

    except Exception as e:
        print(e)

    

def ocisti():
    dir = "static/voucheri/"
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_dir() and not entry.is_symlink():
                shutil.rmtree(entry.path)
            else:
                os.remove(entry.path)