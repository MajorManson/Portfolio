from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from .forms import ContactMeForm
from django.core.mail import send_mail

class ProjectFormView(FormView, SuccessMessageMixin):
    template_name = 'homepage/main.html'
    form_class = ContactMeForm
    success_url = '/'
    success_message = 'Your Form has been successfully submitted!'

    def form_valid(self, form):
        cd = form.cleaned_data
        send_mail(
            f'Contact Inquiry from {cd["name"]}',
            f'{cd["message"]}\n\n{cd["email"]}\n{cd["name"]}',
            settings.EMAIL_HOST_USER,
            ['ajessebo2@gmail.com'],
            fail_silently=False
        )
        return super().form_valid(form)
