from django.shortcuts import render, redirect, get_object_or_404
from .models import Url
from .forms import CreateUrlForm, UpdateUrlForm, DeleteUrlForm
from django.http import JsonResponse, Http404
import random
import string

def generate_short_code():
    chars = string.ascii_letters + string.digits
    shortCode = ''.join(random.choice(chars) for _ in range(10))

    return shortCode

def create_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            url1 = Url.objects.create(url=url, shortCode=generate_short_code())
            url1.save() 

            return render(request, 'kt1_app/created.html', {'url': url1})
        else:
            return render(request, 'kt1_app/create.html', {'error': "URL field is empty"})
    else:
        form = CreateUrlForm()
        return render(request, 'kt1_app/create.html', {'form': form})

def view_url(request, shortCode):
    try:
        url = Url.objects.get(shortCode=shortCode)
        url.accessCount += 1
        url.save()

        return redirect(url.url)
    except Url.DoesNotExist:
        raise Http404("Short URL not found.")

def get_url(request):
    if request.method == 'POST':
        shortCode = request.POST.get('shortCode')
        try:
            url = Url.objects.get(shortCode=shortCode)
            return render(request, 'kt1_app/get.html', {'url': url})
        except Url.DoesNotExist:
            return render(request, 'kt1_app/get.html', {'error': "Short URL not found."})
    return render(request, 'kt1_app/get_form.html')

def delete_url(request):
    if request.method == 'POST':
        form = DeleteUrlForm(request.POST)
        if form.is_valid():
            shortCode = form.cleaned_data['shortCode']
            try:
                url = Url.objects.get(shortCode=shortCode)
                url.delete()
                return render(request, 'kt1_app/deleted.html')
            except Url.DoesNotExist:
                return render(request, 'kt1_app/delete.html', {'error': "Short URL not found."})
    else:
        form = DeleteUrlForm()
    return render(request, 'kt1_app/delete.html', {'form': form})

def update_url(request):
    if request.method == 'POST':
        form = UpdateUrlForm(request.POST)
        if form.is_valid():
            oldShortCode = form.cleaned_data['oldShortCode']
            newShortCode = form.cleaned_data['newShortCode']

            try:
                if Url.objects.filter(shortCode=newShortCode).exists():
                    return render(request, 'kt1_app/update.html', {'error': "Short URL already exists."})

                url = Url.objects.get(shortCode=oldShortCode)
                url.shortCode = newShortCode
                url.save()
                return render(request, 'kt1_app/updated.html', {'url': url})
            except Url.DoesNotExist:
                return render(request, 'kt1_app/update.html', {'error': "Short URL not found."})
    else:
        form = UpdateUrlForm()
    return render(request, 'kt1_app/update.html', {'form': form})




    

