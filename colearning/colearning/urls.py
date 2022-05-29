"""colearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path("profile/", TemplateView.as_view(template_name="profile.html"), name="profile"),
    path("profile/edit", TemplateView.as_view(template_name="edit_profile.html"), name="edit_profile"),
    path("", views.MajlisListView, name="home"),
    path('viewmajlis/<int:pk>/', views.ViewMajlis, name='view_majlis'),
    path('create_majlis/', views.CreateMajlisView, name='create_majlis'),
    path('enrol/<int:pk>/', views.EnrollMajlisView, name='enroll'),
    path('unenrol/<int:pk>/', views.UnenrollMajlisView, name='unenroll'),
    path('viewmajlis/<int:pk>/createpost/', views.CreatePostView, name='create_post'),
    #path('viewmajlis/<int:pk>/viewpost/<int:post_id>/create_comment', views.PostView, name='create_comment'),
    path('viewmajlis/<int:pk>/viewpost/<int:post_id>/', views.PostView, name='view_post'),

]