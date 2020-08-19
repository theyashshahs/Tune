from django.contrib import messages
from django.shortcuts import redirect, render

from users.forms import UserRegisterForm


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created successfully. You can now login 😊')
            return redirect('users:login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/registration.html', {'form': form})
