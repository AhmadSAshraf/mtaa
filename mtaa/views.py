from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, 'home.html')



@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # message.success(request, f'Your account has been updated')
            return render(request,'registration/profile.html')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'registration/profile.html',locals())


@login_required(login_url='/accounts/login/')
def addneighbourhood(request):
    neighbourform = NeighbourhoodForm()
    neighbourform.owner = request.user
    if request.method == "POST":
        neighbourform = NeighbourhoodForm(request.POST,request.FILES)
        if neighbourform.is_valid():
           neighbourform.save()
           return render (request,'home.html')
        else:
           neighbourform=NeighbourhoodForm(request.POST,request.FILES)

    return render(request,'neighbourhood_form.html',{"neighbourform":neighbourform})


@login_required(login_url='/accounts/login/')
def neighbourhood(request):
    neighbourhood = Neighbourhood.objects.all()
    return render(request,'home.html',{"neighbourhood":neighbourhood})
