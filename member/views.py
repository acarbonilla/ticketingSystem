from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# This is for Login and logout

def memberLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('staff')
            else:
                return redirect('authView')

        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Username and Password didn't match. Try Again")
            return redirect('memberLogin')

    else:
        return render(request, 'forms/login.html', {})


def sflogout(request):
    logout(request)
    # messages.success(request, "Successfully Logout.")

    return redirect('home')
