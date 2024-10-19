from django.shortcuts import render
from .models import TeamMember

def team_view(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team/team.html', {'team_members': team_members})
