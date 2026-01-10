from django.shortcuts import render
from .models import Contact,Services,Projects
from django.contrib import messages

# Create your views here.
def home (request):
    services = Services.objects.all()
    projects = Projects.objects.all()
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        message = request.POST['Message']
        Contact.objects.create(
            name = name,
            email = email,
            message = message
        )
        messages.success(request, "Message send successfully")
    context = {
        "services": services,
        "projects":projects
    }
    return render (request,'index.html',context)