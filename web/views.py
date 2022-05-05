from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import Kontakt
from .voucher import create
import mimetypes
from django.conf import settings as django_settings
import os
def index(request):
    file =os.path.join(django_settings.STATIC_ROOT, "voucheri")
    
    for i in os.listdir(file):
        print(i)

    preuzmi = False
    if request.method == "POST":
        form = Kontakt(request.POST)
        if form.is_valid():
            

            od = form.cleaned_data['od']
            do = form.cleaned_data['do']
            sheet = form.cleaned_data['sheet']
        
            code = create(od, do, sheet, request)
            if(code==0):
                messages.success(request, "Uspjeh! Preuzmi datoteku klikom na gumb na izbornoj traci.")
                preuzmi = True
            else:
                messages.error(request, "Greška, Sheet ne postoji.")     
            
        else:
              messages.error(request, "Greška")
        
           
    else:
        form = Kontakt()
      
    
    
    args = {"form":form, "preuzmi": preuzmi }
    return render(request, 'web/index.html', args)


def download_file(request):
    # fill these variables with real values
    fl_path = 'static/finals'
    filename = 'final.pdf'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename

    return response


