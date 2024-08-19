from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def singup(request):
    form = UserCreationForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # Save user data to database
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(request, "home", {"message": "User registered successfully."})
            )

        else:
            return render(
                request,
                "account/singup.html",
                {"error": "Error registering user.", "form": form},
            )

    return render(
        request,
        "account/singup.html",
        {
            "form": form,
        },
    )
