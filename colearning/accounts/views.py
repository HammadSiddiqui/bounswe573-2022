# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Majlis

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



def MajlisListView(request):
    majlis = Majlis.objects.all()
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(majlis)
    return render(request, 'home.html', {'majlis': majlis})



def CreateMajlisView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Majlis(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Majlis()

    return render(request, 'create_majlis.html', {'form': form})