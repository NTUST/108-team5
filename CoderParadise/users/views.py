from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserProfileEditForm
from django.contrib.auth import login, logout, authenticate
from .models import UserProfile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            userProfile = UserProfile.objects.create(user=user, avatar='avatar/defualt.png')
            UserProfile.save(userProfile)
            messages.success(request, f'{username} 創建帳號成功!')
            return redirect('/')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"{username} 你已經成功登入了~")
                return redirect('/')
            else:
                messages.info(request, "密碼或帳號錯誤!!")
        else:
            messages.info(request, "密碼或帳號錯誤!!")

    form = AuthenticationForm()
    return render(request = request, template_name = "users/login.html", context={"form":form})

def profile(request, username):
    user = User.objects.get(username=username)
    userProfile = UserProfile.objects.get(user=user)
    context={
        'userprofile':userProfile
    }

    return render(request, 'users/profile.html', context)

def editProfile(request):
    if request.user.is_authenticated:
        user = request.user
        userProfile = UserProfile.objects.get(user=user)
        if request.method == 'POST':
            form = UserProfileEditForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                
                avatar = request.FILES.get('avatar')

                aboutme = form.cleaned_data.get('aboutme')

                user.email = email
                if avatar != None:
                    userProfile.avatar = avatar
                userProfile.aboutme = aboutme
                user.save()
                userProfile.save()
                messages.success(request, '修改資料成功!')

                return redirect('/users/profile/' + user.username)
        else:
            form = UserProfileEditForm({'email':user.email, 'avatar':userProfile.avatar, 'aboutme':userProfile.aboutme})
            return render(request, 'users/editprofile.html', {'form':form})
    else:
        return redirect('/')