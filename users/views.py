from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your are successfully logged in')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)

    return render(request, 'users/logout.html')


@login_required
def profile_page(request):
    return render(request, 'users/profile.html')
