from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/login/') # wenn neimand angemeldet wird dieser weitergeleitet zum login -> django login annotation
def index(request):
    if request.method == 'POST':
        print("Received data " + request.POST['textMessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textMessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'username': "Sebastian", 'messages': chatMessages})

def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'login/login.html', {'wrongPassword':True, 'redirect':redirect})
    return render(request, 'login/login.html', {'redirect': redirect})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        mail = request.POST['mail']
        pw1 = request.POST['password']
        pw2 = request.POST['password2']
        if pw1 == pw2:
            user = User.objects.create_user(username, mail, pw1)
            return HttpResponseRedirect('/chat')
    return render(request, 'auth/register.html')
