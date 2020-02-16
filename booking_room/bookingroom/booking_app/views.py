from django.shortcuts import render
from .forms import Booking_form
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Booking

# Create your views here.

def booking(request):
    upload = Booking_form()
    if request.method == 'POST':
        upload = Booking_form(request.POST)
        if upload.is_valid():
            upload.save()
            return HttpResponse("""your room is now booked <a href = "{{ url : 'booking'}}">reload</a>""")
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'products'}}">reload</a>""")
    else:
        return render(request, 'booking.html', {'upload_form': upload})
