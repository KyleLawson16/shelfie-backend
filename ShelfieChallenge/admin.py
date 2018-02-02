from django.contrib import admin

# Register your models here.
from ShelfieChallenge.models import Challenge

class ChallengeModelAdmin(admin.ModelAdmin):
	list_display = ["name", "description", "point_value"]
	list_display_links = ["name"]

	search_fields = ["name", "description", "point_value"]
	class Meta:
		model = Challenge

admin.site.register(Challenge, ChallengeModelAdmin)
