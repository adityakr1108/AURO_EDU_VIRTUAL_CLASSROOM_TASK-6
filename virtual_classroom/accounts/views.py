from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def dashboard_view(request):
    if request.user.role == 'teacher':
        return render(request, 'accounts/teacher_dashboard.html', {'user': request.user})
    else:
        return render(request, 'accounts/student_dashboard.html', {'user': request.user})



def video_chat_room(request, room_name):
    return render(request, 'video/video_chat.html', {'room_name': room_name})
