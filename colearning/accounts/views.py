# accounts/views.py
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Majlis
from .forms import MajlisForm

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



def MajlisListView(request):
    majlis = Majlis.objects.all()
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(majlis)
    return render(request, 'home.html', {'majlis': majlis})

def ViewMajlis(request, pk):
    majlis = get_object_or_404(Majlis, pk=pk)
    print("Yelo",majlis.people.all())
    return render(request, 'view_majlis.html', {'majlis': majlis})


@login_required
def CreateMajlisView(request):
    # if this is a POST request we need to process the form data

    form = MajlisForm()
    # check whether it's valid:
    if request.method == 'POST':
        #print(request.user)
        form = MajlisForm(request.POST)
        if form.is_valid():
            #form.people = request.user #UserProfile.objects.get(user=self.request.user)  # use your own profile here
            majlisObj = form.save(commit=False)
            majlisObj.author  = request.user
            majlisObj.save()
            majlisObj.people.add(request.user)
            print(majlisObj.id)
            return redirect('view_majlis', pk=majlisObj.id)
            #return redirect('home')
    else:
        #print(form)
        context = {"form" : form}


    return render(request, 'create_majlis.html', {'form': form})


@login_required
def EnrollMajlisView(request):
    #print(request)
    return HttpResponseRedirect('/enrolled/')