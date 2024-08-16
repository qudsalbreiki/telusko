from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):#request what you get from the client
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = "The city never sleeps"
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer = False


    # dest2 = Destination()
    # dest2.name = 'Hyderabad'
    # dest2.desc = "First Biryani, then sherwani"
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 650
    # dest2.offer = True


    # dest3 = Destination()
    # dest3.name = 'Bengaluru'
    # dest3.desc = "Beutiful city"
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 750
    # dest3.offer = False

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})  #you have to get back in a response
