from django.forms import ModelForm
from .models import Contect, Appointment


class ContactForm(ModelForm):
    class Meta:
        model = Contect
        fields = '__all__'


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
