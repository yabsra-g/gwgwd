from django.shortcuts import render, get_object_or_404
from .models import Artwork, Artist, Activity, Country

def home(request):
    latest_activities = Activity.objects.all()[:3]
    return render(request, 'core/home.html', {'latest_activities': latest_activities})

def projects(request):
    # Get list of countries from choices
    # Get list of countries
    countries = Country.objects.all().order_by('name')
    return render(request, 'core/projects.html', {'countries': countries})

def project_list_by_country(request, category):
    artworks = Artwork.objects.filter(country__name=category)
    country = Country.objects.filter(name=category).first()
    return render(request, 'core/project_list.html', {
        'artworks': artworks,
        'category': category,
        'country': country
    })

def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'core/artwork_detail.html', {'artwork': artwork})

def about(request):
    project_leaders = Artist.objects.filter(role='Team Leader')
    return render(request, 'core/about.html', {
        'project_leaders': project_leaders,
    })

def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'core/activity_list.html', {'activities': activities})


def activity_detail(request, slug):
    activity = get_object_or_404(Activity, slug=slug)
    return render(request, 'core/activity_detail.html', {'activity': activity})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'core/artist_detail.html', {'artist': artist})
