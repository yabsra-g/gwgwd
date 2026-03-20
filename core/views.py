from django.shortcuts import render, get_object_or_404
from .models import Artwork, Artist, Activity, Country
import json
import os
from django.conf import settings
from xml.etree import ElementTree as ET


def home(request):
    latest_activities = Activity.objects.all()[:3]
    return render(request, 'core/home.html', {'latest_activities': latest_activities})

def get_svg_data():
    svg_path = os.path.join(settings.BASE_DIR, 'core', 'static', 'core', 'world.svg')
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    data = {}
    # Remove namespace prefix from tags
    for elem in root.iter():
        elem.tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
    
    for elem in root.iter():
        elem_id = elem.get('id')
        if not elem_id or elem_id == 'world-map':
            continue
        # Get inner content (child paths) or the element itself
        inner = ''
        if list(elem):  # has children (like <g>)
            for child in elem:
                child.tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
                inner += ET.tostring(child, encoding='unicode')
        else:
            inner = ET.tostring(elem, encoding='unicode')
        data[elem_id] = inner
    return data

SVG_DATA = get_svg_data()  # parsed once at startup

def projects(request):
    countries = Country.objects.all().order_by('name')
    active_countries = {}
    active_countries_map = []
    
    for country in countries:
        if country.iso_code and country.artworks.exists():
            active_countries[country.iso_code] = country.name
            iso = country.iso_code.lower()
            if iso in SVG_DATA:
                active_countries_map.append({
                    'iso_code': iso,
                    'name': country.name,
                    'svg_path': SVG_DATA[iso],
                })
    
    return render(request, 'core/projects.html', {
        'countries': countries.filter(artworks__isnull=False).distinct(),
        'active_countries_json': json.dumps(active_countries),
        'active_countries_map': active_countries_map,  # list, not json
    })


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
    project_leaders = Artist.objects.filter(role='Team Leader').order_by('name')
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
    selected_works = artist.artworks.order_by('?')[:4]
    return render(request, 'core/artist_detail.html', {
        'artist': artist,
        'selected_works': selected_works,
    })
