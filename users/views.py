from django.shortcuts import render, redirect
# from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

# def sign_up(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#         return render(request, 'users/register.html', { 'form': form})  
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})