from django.shortcuts import render
from userData.models import UserData

# Create your views here.
def show_main(request):
    context = {"user": "Guest"}

    if request.user.is_authenticated:
        user_data = UserData.objects.get(user=request.user)

        context["user"] = request.user
        context["user_data"] = user_data
        
    return render(request, "main.html", context)