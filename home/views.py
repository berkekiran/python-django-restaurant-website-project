from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting, ContactForm, ContactFormMessage
from product.models import Product


def index(request):
    sliderData = Product.objects.all()[:3]
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'home', 'sliderData': sliderData}
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'aboutus'}
    return render(request, 'aboutus.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'references'}
    return render(request, 'references.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message sent successfully. Thanks.")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'setting': setting, 'form': form}
    return render(request, 'contact.html', context)


def faq(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'faq'}
    return render(request, 'faq.html', context)