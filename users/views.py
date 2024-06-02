from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """ yeni istafadechi uchun qeydiyyat"""
    if request.method != 'POST':
        # Blank qeydiyyat formu
        form = UserCreationForm()
    else:
        # artiq doldurulmush formu process et
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # yeni istifadechini log et ve index sehifeye gonder
            login(request, new_user)
            return redirect('learning_logs:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)
