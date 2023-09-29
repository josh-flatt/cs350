from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.

def helloView(request):
    return render(request, "helloView.html")

def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    # You can fetch related data like experiences, education, skills, etc.
    experiences = user.experience_set.all()
    educations = user.education_set.all()
    skills = user.skill_set.all()

    context = {
        'user': user,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
    }

    return render(request, 'user_profile.html', context)