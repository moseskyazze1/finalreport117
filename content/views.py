from django.shortcuts import render
from .models import Project, Experience, Contact  # Ensure all models are imported

# View for listing projects
def projects_list(request):
    projects = Project.objects.all()
    return render(
        request,
        "content/projects_list.html",
        {"projects": projects}
    )

# View for listing experiences
def experience_list(request):
    experiences = Experience.objects.all()
    return render(
        request,
        "content/experience_list.html",
        {"experiences": experiences} 
    )

# View for listing contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(
        request,
        "content/contact_list.html",
        {"contacts": contacts} 
    )
