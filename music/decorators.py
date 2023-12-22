from django.shortcuts import redirect


def check_authentication(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Замените 'login' на ваше имя URL для страницы входа в систему

    return wrapper
