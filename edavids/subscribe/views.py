from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from .models import Subscriber
from .forms import SubscriberForm
import random
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.core import mail
from django.views.generic.edit import CreateView


# Create your views here.
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


class SubscriberView(CreateView):
    model = Subscriber
    form_class = SubscriberForm
    template_name = "includes/footer.html"
    success_url = '/'

    def form_valid(self, form):
        email = form.instance.email
        form.instance.conf_num = random_digits()
        conf_num = form.instance.conf_num
        from_email="noreply@edavids.me"
        to_emails=email
        subject='Newsletter Confirmation',
        html_message = render_to_string('emails/newsletter.html', {'email': email, 'conf_num': conf_num, 'url': self.request.build_absolute_uri('/confirm/')})
        plain_message = strip_tags(html_message)
        send_mail(subject, plain_message, from_email, [to_emails], html_message=html_message)
        return super().form_valid(form)



def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'includes/footer.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'includes/footer.html', {'email': sub.email, 'action': 'denied'})


def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'includes/footer.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'includes/footer.html', {'email': sub.email, 'action': 'denied'})


