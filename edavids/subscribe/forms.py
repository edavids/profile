from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(label='Your email',
                             max_length=150,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Subscriber
        fields = ['email']


    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        qs = Subscriber.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("You have already subscribed")
        return super().clean()