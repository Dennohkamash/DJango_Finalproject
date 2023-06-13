from django.shortcuts import render, redirect
from .models import Listing
from .forms import listing_form

# Create your views here.

def listings(request):
    listings = Listing.objects.all()
    context = {
        "listings":listings
    }
    return render(request, "listings.html", context)

def listing(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing":listing
    }
    return render(request, "listing.html", context)

def create_listing(request):
    form = listing_form()
    if request.method == "POST":
        form = listing_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form    
    }
    return render(request, "create_listing.html", context)

def property(request):
    listings = Listing.objects.all()
    context = {
        "listings":listings
    }
    return render (request, 'property.html', context)

def blogs(request):
    return render(request, 'blogs.html')

def contact_us(request):
    return render(request, 'contact-us.html')