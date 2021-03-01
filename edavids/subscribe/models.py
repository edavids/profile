from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True, null=True, blank=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self): 
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = RichTextUploadingField()

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = Subscriber.objects.filter(confirmed=True)
        for sub in subscribers:
            email = sub.email
            from_email="noreply@edavids.me"
            to_emails=email
            subject=self.subject
            html_message = render_to_string('emails/new_newsletter.html', {'email': email, 'conf_num':sub.conf_num, 'url': self.request.build_absolute_uri('/delete/')})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, from_email, [to_emails], html_message=html_message)

            send_mail(
                from_email="noreply@edavids.me",
                to_emails=sub.email,
                subject=self.subject,
                html_message=contents + (
                    '<br><a href="{}/delete/?email={}&conf_num={}">Unsubscribe</a>.').format(request.build_absolute_uri('/delete/'), sub.email, sub.conf_num)
                    )