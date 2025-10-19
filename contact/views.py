

# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],  # your email
                fail_silently=False,
            )


            messages.success(request, '✅ Your message has been sent successfully!')
            form = ContactForm()  # clear form
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
