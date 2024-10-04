from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method =="POST":

        
        form = ContactForm(request.POST)

        if form.is_valid():
            print("Sending")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_message = f"Name:{name}\nEmail:{email}\nMessage:{message}"

            send_mail(
                "Email from" + name,
                message,
                email,
                ['kyazzemoses123@yahoo.com']
            )
        else:
            print("Invalid Form")
    else:

        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})
