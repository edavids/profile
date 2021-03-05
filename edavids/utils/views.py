from .forms import ContactForm
from django.http import HttpResponse, JsonResponse
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form": contact_form,
    }
    if contact_form.is_valid():
        form = contact_form
        name = form.cleaned_data['name']
        company = form.cleaned_data['company']
        subject = "Contact From Website"
        from_email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        message = "{name} from {company} - has sent a message: \n\n Phone: ({phone}) \n\n Subject: {subject} \n\n Email: {email} \n\n Message: {message}".format(name=name, phone=phone, company=company, subject=subject, email=from_email, message=form.cleaned_data['message'])
        try:
            send_mail(
                subject, 
                message, 
                from_email, 
                [settings.DEFAULT_FROM_EMAIL], 
                fail_silently=False
            )
        except BadHeaderError:
            return HttpResponse('Invalid Header Found')
        messages.success(request, "Your message has been submited successfully!")
        return redirect('home')
    return render(request, "pages/contact.html", context)
