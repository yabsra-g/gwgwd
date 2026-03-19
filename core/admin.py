from django.contrib import admin
from .models import Artwork, Artist, Activity, Country

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'country', 'created_at')
    list_filter = ('country', 'artist')
    search_fields = ('title', 'artist__name')

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

