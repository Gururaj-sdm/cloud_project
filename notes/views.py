# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

from .models import Note
from .forms import NoteForm

from django.contrib.auth.decorators import login_required


@login_required
def list_notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request,'list_notes.html',{'notes':notes})

@login_required
def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('/dashboard/')
    else:
        form = NoteForm()

    return render(request,'add_note.html',{'form':form})



@login_required
def delete_note(request, id):

    note = get_object_or_404(Note, id=id, user=request.user)

    note.delete()

    return redirect('/dashboard/')

def share_note(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, 'share_note.html', {'note': note})

from django.contrib.auth import authenticate, login

def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

    return render(request, 'login.html')

def signup_view(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username=username, password=password)
            return redirect('/')
        except IntegrityError:
            error = 'That username is already taken. Please choose another.'

    return render(request, 'signup.html', {'error': error})

def logout_view(request):

    logout(request)

    return redirect('/')