from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, f'{username} 創建帳號成功!')
            return redirect('/QA/')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form})