from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.



from basketapp.models import Team, Player, Coach, Match


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['thumb','name','logo']
    search_fields = ['name']

    def thumb(self,obj):
        return mark_safe("<img src='%s' width='40' height='40'>" %obj.logo.url)
    thumb.allow_tags = True
    thumb.__name__= 'logo'

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name','image','thumb']
    list_filter = ['team','birthday']
    search_fields = ['name', 'alias', 'rut']

    def thumb(self,obj):
        print(obj.image.url)
        return mark_safe("<img src='%s' width='40' height='40'>" %obj.image.url)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['namematch']
