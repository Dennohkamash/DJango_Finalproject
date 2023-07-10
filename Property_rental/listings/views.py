from django.shortcuts import render, redirect
from .models import Listing, User
from .forms import listing_form, MyUserCreationForm

#users
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
#test
    
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'signin.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'registration/signup.html', {'form': form})


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

@login_required(login_url='login')
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