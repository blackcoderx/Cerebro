from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm , RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile,School


def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home page or dashboard after successful login
            else:
                form.add_error(None, 'Invalid username or password')
    return render(request, 'base/login.html', {'form': form})




def register(request):
    schools = School.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)


        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) # takes the user's password, hash it and store it
            user.first_name = form.cleaned_data['name']  # Save the name to the user's first_name field

            school_name = request.POST.get('school_name')
            school, created = School.objects.get_or_create(name=school_name)

            user.save()
            profile = Profile(user=user)
            profile.name = form.cleaned_data['name']
            profile.school_name = form.cleaned_data['school_name']
            profile.age = form.cleaned_data['age']
            profile.course = form.cleaned_data['course']
            # profile.level_of_education = form.cleaned_data['level_of_education']
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = RegistrationForm()

    context = {'form': form, 'schools': schools}
        
    return render(request, 'base/register.html', context)








def homepage(request):
  return render(request,'base/base.html')


def welcome_page(request):
  return render(request,'base/welcome.html')