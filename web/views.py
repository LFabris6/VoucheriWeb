from django.shortcuts import render, redirect
from django.http import request
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import Kontakt


def index(request):

    if request.method == "POST":
        form = Kontakt(request.POST)
        if form.is_valid():

            email = form.cleaned_data.get('email')
            poruka = form.cleaned_data.get('poruka')
            try:
                send_mail(
                email,
                poruka,
                'adrtiaticwebdev@gmail.com',
                ['adrtiaticwebdev@gmail.com'],
                fail_silently=False,
                )
                messages.success(request, "Hvala vam, vaša poruka je poslana, odgovoriti ćemo vam u što kraćem roku.")
                return redirect("/#kontakt")
            except:
                messages.error(request, "Došlo je do pogreške sa naše strane, molimo direktno nas kontaktirajte na našu email adresu. Hvala vam.")
           
    else:
        form = Kontakt()
    
    
    args = {"form":form}
    return render(request, 'web/index.html', args)