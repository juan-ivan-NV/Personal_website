from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
# Create your views here.

def contact(request):

    '''if request.method =="POST":

        myForm = ContactForm(request.POST)

        if myForm.is_valid():
            
            infForm=myForm.cleaned_data

            send_mail(infForm['Name'], infForm['Content'], infForm.get('Email',''), ['coldcram14@hotmail.com'],)

            return render(request, 'contact.html')

    else:''' 

    myForm = ContactForm()

    return render(request, 'contact/contact.html', {'form': myForm})