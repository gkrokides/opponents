from django.contrib import admin
from .models import Player, Rating, Sport


class PlayerAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'self_rating', 'sports')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Rating)
admin.site.register(Sport)


