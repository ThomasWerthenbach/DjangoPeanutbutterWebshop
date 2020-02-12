from django.shortcuts import render, redirect
from .forms import *
from .models import PeanutButter

def index(request):
    peanuts = PeanutButter.objects.all()
    context = {'peanutbutter': peanuts}
    return render(request, 'lecture/index.html', context)

def new(request):
    if request.POST:
        peanutform = PeanutButterForm(request.POST)
        peanutform.save()
        return redirect(index)
    context = {'form': PeanutButterForm}
    return render(request, 'lecture/new.html', context)


def edit(request, peanut_id):
    peanutbutter = PeanutButter.objects.get(id=peanut_id)
    if request.POST:
        peanutform = PeanutButterForm(request.POST, instance=peanutbutter)
        peanutform.save()
        return redirect(index)
    context = {'form': PeanutButterForm(instance=peanutbutter)}
    return render(request, 'lecture/new.html', context)