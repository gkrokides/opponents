from django.contrib import admin
from .models import Player, Rating, Sport, Game


# class PlayerAdmin(admin.ModelAdmin):
#     fields = ('first_name', 'last_name', 'sports', 'self_rating')

admin.site.register(Player)
admin.site.register(Rating)
admin.site.register(Sport)
admin.site.register(Game)


