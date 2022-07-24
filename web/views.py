from distutils.log import error
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import Kontakt
from .voucher import create, ocisti
import mimetypes
from django.conf import settings as django_settings
import os
from django.views.generic import View
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice
from firebase_admin import firestore, initialize_app

import firebase_admin
from firebase_admin import credentials, messaging


def apitest(request):

    return render(request, 'web/apitest.html', {})



class ServiceWorkerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'web/firebase-messaging-sw.js', content_type="application/x-javascript")


def test(request):

    print(FCMDevice.objects.send_message(
    Message(notification=Notification(title="titdle", body="bodfafy", image="imadaage_url"))
    ))
  
 



    return render(request, 'web/test.html', {})



def index(request):
    ocisti()
    preuzmi = False
    if request.method == "POST":
        form = Kontakt(request.POST)
        if form.is_valid():
            

            od = form.cleaned_data['od']
            do = form.cleaned_data['do']
            sheet = form.cleaned_data['sheet']
        
            #code = create(od, do, sheet, request)
            code=0
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

