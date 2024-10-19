import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from datetime import datetime, timedelta

# Set up Django environment

from about.models import AboutUs   
from blog.models import BlogPost
from event.models import Event
from services.models import Service
from team.models import TeamMember
from contact.models import Location
from testimonial.models import Testimonial

def create_about_us():
    AboutUs.objects.create(
        title="About Us Title",
        subtitle="Subtitle of About Us",
        description="This is a description about the company.",
        image="C:/Users/HPz/Desktop/school/smart.jpg",
        more_details_link="http://example.com/more-details"
    )

def create_blog_posts(num_posts=5):
    for _ in range(num_posts):
        BlogPost.objects.create(
            title=f"Blog Post Title {_+1}",
            author="Author Name",
            date_posted=datetime.now() - timedelta(days=random.randint(0, 30)),
            content="This is the content of the blog post.",
            image="C:/Users/HPz/Desktop/school/smart.jpg"
        )

def create_events(num_events=3):
    for _ in range(num_events):
        Event.objects.create(
            title=f"Event Title {_+1}",
            date=datetime.now().date() + timedelta(days=random.randint(1, 30)),
            time=datetime.now().time(),
            location="Event Location",
            description="This is a description of the event.",
            image="C:/Users/HPz/Desktop/school/smart.jpg"
        )

def create_locations(num_locations=2):
    for _ in range(num_locations):
        Location.objects.create(
            name=f"Location Name {_+1}",
            address="123 Main St, Anytown, USA",
            map_iframe="<iframe src='https://www.google.com/maps/embed?pb=!1s...'></iframe>"
        )

def create_services(num_services=4):
    for _ in range(num_services):
        Service.objects.create(
            title=f"Service {_+1}",
            description="Description of the service offered.",
            icon_class="icon-class-example",
            image_serv="C:/Users/HPz/Desktop/school/smart.jpg"
        )

def create_team_members(num_members=5):
    for _ in range(num_members):
        TeamMember.objects.create(
            name=f"Team Member {_+1}",
            position="Team Member Position",
            image="C:/Users/HPz/Desktop/school/smart.jpg",  # Update with your image path
            facebook_link="http://facebook.com/example",
            twitter_link="http://twitter.com/example",
            instagram_link="http://instagram.com/example"
        )

def create_testimonials(num_testimonials=3):
    for _ in range(num_testimonials):
        Testimonial.objects.create(
            name=f"Tester {_+1}",
            profession="Profession of Tester",
            message="This is a testimonial message.",
            image="C:/Users/HPz/Desktop/school/smart.jpg",  # Update with your image path
            rating=random.randint(1, 5)
        )

if __name__ == "__main__":
    create_about_us()
    create_blog_posts()
    create_events()
    create_locations()
    create_services()
    create_team_members()
    create_testimonials()
    print("Dummy data creation completed successfully!")
