# from curses.ascii import EM
from unicodedata import name
from django.shortcuts import render, redirect
from . import models
from .models import Service, Team, Contect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.conf import settings
from .forms import ContactForm, AppointmentForm
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse


# Create your views here.
def Home(request):
    services = Service.objects.all()
    data = {
        'services': services
    }
    return render(request, 'pages/home.html', data)


def About_us(request):
    return render(request, 'pages/about.html')


def Services(request):
    services = Service.objects.all()
    data = {
        'services': services
    }
    return render(request, 'pages/services.html', data)


def Single_Service(request):
    # services=Service.objects.all()
    # data={
    #     'services':services
    # }
    return render(request, 'pages/single_service.html')


def Teams(request):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/team.html', data)


def Appointment(request):
    if request.method == 'POST':
        fm = AppointmentForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Contact request submitted successfully.')
            # messages.add_message(request, messages.SUCCESS, 'Contact request submitted successfully !!')
            return render(request, 'pages/contect.html', {'form': ContactForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, fm.errors)
    else:
        fm = AppointmentForm()
    return render(request, 'pages/appointment.html', {'form': fm})


def Contect_us(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = "Website Inquiry"
                body = f"name: {form.cleaned_data['name']}\nemail: {form.cleaned_data['email']}\nmessage: {form.cleaned_data['message']}"
                form.save()

                try:
                    msg = EmailMessage('heading',
                       body, to=['muneeb9166@gmail.com'])
                    msg.send()
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                # Success message
                messages.add_message(request, messages.SUCCESS, 'Contact details sent successfully!')
                return render(request, 'pages/success_message.html')

        form = ContactForm()
        return render(request, 'pages/contect.html', {'form': form})


    # if request.method == 'POST':
    #     fm = ContactForm(request.POST)
    #     if fm.is_valid():
    #         fm.save()
    #         # messages.success(request, 'Contact request submitted successfully.')
    #         messages.add_message(request, messages.SUCCESS, 'Contact request submitted successfully !!')
    #         # return render(request, 'pages/contect.html', {'form': ContactForm(request.GET)})
    #     # else:
    #     #     messages.error(request, 'Invalid form submission.')
    #     #     messages.error(request, fm.errors)
    # else:
    #     fm = ContactForm()
    # return render(request, 'pages/contect.html', {'form': fm})
