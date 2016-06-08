from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.shortcuts import redirect, render


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'account/signup.html', context)