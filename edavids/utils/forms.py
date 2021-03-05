from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .tasks import send_message_task


class ContactForm(forms.Form):
    email = forms.EmailField(label="Your email please?", required=True)
    phone = forms.CharField(label="Your phone number please?", required=True)
    name = forms.CharField(label="Your name please?", required=True)
    company = forms.CharField(
        label="Company name",
        help_text="Leave blank if not messaging for a company",
        required=False,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        label="Let us get your message",
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control border-form-control required"
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("email", css_class="form-group col-6 mb-0"),
                Column("phone", css_class="form-group col-6 mb-0"),
                Column("name", css_class="form-group col-12 mb-0"),
                Column("company", css_class="form-group col-12 mb-0"),
                Column("message", css_class="form-group col-12 mb-0"),
                css_class="form-row",
            ),
            Submit(
                "submit",
                "Send ",
                css_class="button h-translatey-3 bg-dark rounded-pill btn-block",
            ),
        )
