from django.contrib import admin

# Register your models here.
from ShelfieGame.models import Game

class GameModelAdmin(admin.ModelAdmin):
	list_display = ["date", "organization", "home_team", "away_team"]
	list_display_links = ["date", "organization"]

	search_fields = ["date", "organization", "home_team"]
	class Meta:
		model = Game

admin.site.register(Game, GameModelAdmin)
