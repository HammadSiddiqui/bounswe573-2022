# accounts/views.py
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Majlis, Post, Comment
from .forms import MajlisForm, PostForm, CommentForm

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

            return redirect('view_majlis', pk=majlisObj.id)
            #return redirect('home')
    else:
        #print(form)
        context = {"form" : form}


    return render(request, 'create_majlis.html', {'form': form})


@login_required
def EnrollMajlisView(request, pk):
    print(request)
    majlis = get_object_or_404(Majlis, pk=pk)
    majlis.people.add(request.user)
    return redirect('view_majlis', pk=majlis.id)

@login_required
def UnenrollMajlisView(request, pk):
    print(request)
    majlis = get_object_or_404(Majlis, pk=pk)
    majlis.people.remove(request.user)
    return redirect('view_majlis', pk=majlis.id)


#View to add a new post in a majlis
@login_required
def CreatePostView(request, pk):
    form = PostForm()
    # check whether it's valid:
    if request.method == 'POST':
        #print(request.user)
        form = PostForm(request.POST)
        if form.is_valid():
            #form.people = request.user #UserProfile.objects.get(user=self.request.user)  # use your own profile here
            PostObj = form.save(commit=False)
            PostObj.author  = request.user
            PostObj.save()
            majlis = get_object_or_404(Majlis, pk=pk)
            majlis.posts.add(PostObj)

            return redirect('view_majlis', pk=pk)
            #return redirect('home')
    else:
        #print(form)
        context = {"form" : form}
    return render(request, 'create_post.html', {'form': form, 'majlis_id': pk})



@login_required
def PostView(request, pk, post_id):
    print(request)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'view_post.html', {'post' : post})


##ADD A NEW COMMENT View
@login_required
def CreateCommentView(request, pk):
    form = CommentForm()
    # check whether it's valid:
    if request.method == 'POST':
        #print(request.user)
        form = CommentForm(request.POST)
        if form.is_valid():
            #form.people = request.user #UserProfile.objects.get(user=self.request.user)  # use your own profile here
            commentObj = form.save(commit=False)
            commentObj.author  = request.user
            commentObj.save()
            post = get_object_or_404(Post, pk=pk)
            post.comments.add(commentObj)

            return redirect('view_majlis', pk=pk)
            #return redirect('home')
    else:
        #print(form)
        context = {"form" : form}
    return render(request, 'create_post.html', {'form': form, 'majlis_id': pk})