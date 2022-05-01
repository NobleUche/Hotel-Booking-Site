
from django.shortcuts import redirect, render
from .forms import reservation_form

# Create your views here.

def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')


def rooms(request):
    return render(request,'rooms.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')


def booking(request):
    if request.method == 'POST':
        form = reservation_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
    else:
        form = reservation_form
        return render(request,'booking.html', {'form':form})
 