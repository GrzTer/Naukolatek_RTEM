from django.shortcuts import render


def home_view(request):
    context = {"message": "Witaj na stronie głównej."}
    return render(request, "home.html", context=context)


def about_view(request):
    return render(request, "O_Projekcie.html")
