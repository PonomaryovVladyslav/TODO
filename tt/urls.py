"""tt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from todo.views import Registration, NotesListView, Login, Logout, NotesCreateView, NoteDeleteView, NoteShareView, \
    NotesSharedListView

urlpatterns = [
    path('', NotesListView.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('admin/', admin.site.urls),
    path('create_note/', NotesCreateView.as_view(), name='create_note'),
    path('delete_note/<int:pk>/', NoteDeleteView.as_view(), name='delete_note'),
    path('share_note/<int:pk>/', NoteShareView.as_view(), name='share_note'),
    path('shared/', NotesSharedListView.as_view(), name='shared')
]
