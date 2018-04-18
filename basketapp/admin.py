from django.contrib import admin

# Register your models here.



from basketapp.models import Team, Player, Coach, Match


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['logo']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['photograpy']
    list_filter = ['name','birthday']

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['namematch']


# @admin.register(Song)
# class SongAdmin(admin.ModelAdmin):
#     list_display = ('name','duration','album')
#     list_filter = ('album','duration')
