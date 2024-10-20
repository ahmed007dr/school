
from django.shortcuts import render
from about.models import AboutUs  
from blog.models import BlogPost   
from contact.models import Location 
from testimonial.models import Testimonial 
from team.models import TeamMember
from event.models import Event
from services.models import Service

def homepage(request):
    about_info = AboutUs.objects.first()
    blog_posts = BlogPost.objects.all().order_by('-date_posted')[:3]  
    location = Location.objects.first()  
    testimonials = Testimonial.objects.all()  
    team_members = TeamMember.objects.all()  
    events = Event.objects.all().order_by('date', 'time')  
    services = Service.objects.all()  

    context = {
        'about_info': about_info,
        'blog_posts': blog_posts,
        'location': location,
        'testimonials': testimonials,  
        'team_members': team_members,  
        'events': events,  
        'services': services,   }

    return render(request, 'homepage/home.html', context)
