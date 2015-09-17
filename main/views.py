from django.shortcuts import render
from models import Volunteer


def index(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'main/volunteers.html', {'volunteers': volunteers})

def volunteer_view(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    return render(request, 'main/volunteer.html', {'volunteer': volunteer})