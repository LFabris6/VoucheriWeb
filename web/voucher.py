
import os
import shutil
from django.conf import settings as django_settings
import gspread
from mailmerge import MailMerge
from docx import Document
from docxcompose.composer import Composer

template = "static/api/voucher.docx"
composed = "static/finals/final.docx"
files = []

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
    
 
    try:
        spoji()
    except Exception as e:
        print(e)
    ocisti()
   
    return 0


def ispuni(ime, prezime, broj, gmail,datum):
    try:
        print("pocetak docx " + ime)
        document = MailMerge(template)
        document.merge(Ime=ime, prezime=prezime, email=gmail, broj = broj, rodenje=datum)
     
        file =os.path.join(django_settings.STATIC_ROOT)
        voucher_path = file + r"\voucheri\voucher" + str(broj) + ".docx"
   
        document.write(voucher_path)
        print("docx sejvan " + ime)

        

    except Exception as e:
        print(e)



def spoji():
    all_dir = "static/voucheri/"
    for i in os.listdir(all_dir):
        path = os.path.join(all_dir, i)
        files.append(path)
    
    
    result = Document(files[0])
    result.add_page_break()
    composer = Composer(result)

    for i in range(1, len(files)):
        doc = Document(files[i])

        if i != len(files) - 1:
            doc.add_page_break()

        composer.append(doc)

    composer.save(composed)
    

def ocisti():
    dir = "static/voucheri/"
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_dir() and not entry.is_symlink():
                shutil.rmtree(entry.path)
            else:
                os.remove(entry.path)