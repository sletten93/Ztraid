from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        return render(request, 'app/public/index.html')
    else:
        return render(request, 'app/public/not_auth.html')
