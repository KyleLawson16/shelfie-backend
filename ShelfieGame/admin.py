from django.contrib import admin

# Register your models here.
from ShelfieGame.models import Game, GameChallenge

class GameModelAdmin(admin.ModelAdmin):
	list_display = ["random_game_id", "date", "organization", "home_team"]
	list_display_links = ["date"]

	search_fields = ["date", "organization", "home_team"]
	class Meta:
		model = Game

admin.site.register(Game, GameModelAdmin)

class GameChallengeModelAdmin(admin.ModelAdmin):
	list_display = ["game", "challenge"]
	list_display_links = ["game"]

	search_fields = ["game", "challenge"]
	class Meta:
		model = GameChallenge

admin.site.register(GameChallenge, GameChallengeModelAdmin)
